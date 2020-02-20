using Blank_Pages_Backend.Data;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using System.Collections.Generic;
using System.Linq;

namespace Blank_Pages_Backend.Models
{
    public class DataProvider
    {
        private BlankPagesDbContext _context;

        #region General

        public DataProvider(BlankPagesDbContext dbcontext)
        {
            _context = dbcontext;
        }

        private void EntryUpdater(EntityEntry entry, object updatedEntry)
        {
            dynamic update;

            switch (updatedEntry.GetType().Name)
            {
                case nameof(Article):
                    update = (Article)updatedEntry;
                    break;
                case nameof(Author):
                    update = (Author)updatedEntry;
                    break;
                case nameof(Source):
                    update = (Source)updatedEntry;
                    break;
                default:
                    update = string.Empty;
                    break;
            }

            if (update is string)
            {
                return;
            }

            foreach (var prop in entry.Properties)
            {
                var newVal = update.GetType().GetProperty(prop.Metadata.Name).GetValue(update, null);

                if (prop.CurrentValue != newVal)
                {
                    prop.CurrentValue = newVal;
                }
            }

            _context.SaveChanges();
        }
        #endregion

        #region Articles

        public List<int> GetAllArticleIds()
        {
            return _context.Articles.Select(a => a.Id).ToList();
        }

        public List<Article> GetAllArticles()
        {
            return _context.Articles.Select(a => a).ToList();
        }

        public List<Article> GetFilteredArticles(string phrase)
        {
            var filtered = _context.Articles.Where(a => a.Title.Contains(phrase) || a.SubTitle.Contains(phrase) || GetAuthorById(a.ArticleAuthor.Id).Name.Contains(phrase))
                .Select(a => a).ToList();
            filtered.Sort();
            return filtered;

        }

        public Article GetArticleById(int id)
        {
            return _context.Articles.Find(id);
        }

        public Article GetArticleByTitle(string title)
        {
            return _context.Articles.FirstOrDefault(a => a.Title.Equals(title) || a.SubTitle.Equals(title));
        }

        public List<Article> GetArticlesByAuthor(string authorName)
        {
            return _context.Authors.Where(a => a.Name.Equals(authorName))
                .Select(a => a.ArticlesWritten.ToList())
                .FirstOrDefault(list => list is List<Article>);
        }

        public int AddArticle(Article article)
        {
            var entry = _context.Articles.Add(article);
            _context.SaveChanges();
            return entry.Entity.Id;
        }

        public void UpdateArticle(Article article)
        {
            var entry = _context.Articles.Update(GetArticleById(article.Id));

            if (entry != null)
            {
                EntryUpdater(entry, article);
            }
            else
            {
                AddArticle(article);
            }
        }

        public void DeleteArticle(int id)
        {
            _context.Articles.Remove(GetArticleById(id));
            DeleteSourcesByArticleId(id);
        }

        public void DeleteArticlesByAuthor(string name)
        {
            var articles = GetArticlesByAuthor(name);
            articles.ForEach(rtcl => rtcl.Sources.ToList().ForEach(s => _context.Sources.Remove(s)));
            _context.Articles.RemoveRange(articles);
            _context.SaveChanges();
        }

        #endregion

        #region Sources

        public List<Source> GetAllSources()
        {
            var sources = _context.Sources.Select(s => s).ToList();
            sources.Sort();
            return sources;
        }

        public Source GetSourceById(int id)
        {
            return _context.Sources.Find(id);
        }

        public Source GetSourceByName(string name)
        {
            return _context.Sources.FirstOrDefault(s => s.Name.Equals(name));
        }

        public List<Source> GetSourcesByArticleId(int id)
        {
            return _context.Sources.Where(s => s.ParentArticle.Id == id).Select(s => s).ToList();
        }

        public void AddSource(Source source)
        {
            _context.Sources.Add(source);
            _context.SaveChanges();
        }

        public void UpdateSource(Source source)
        {
            var entry = _context.Sources.Update(GetSourceById(source.Id));

            if (entry != null)
            {
                EntryUpdater(entry, source);
            }
            else
            {
                AddSource(source);
            }
        }

        public void DeleteSourceById(int id)
        {
            _context.Sources.Remove(GetSourceById(id));
            _context.SaveChanges();
        }

        private void DeleteSourcesByArticleId(int id)
        {
            var sourcesToRemove = GetSourcesByArticleId(id);
            _context.Sources.RemoveRange(sourcesToRemove);
            _context.SaveChanges();
        }

        #endregion

        #region Authors

        public Author GetAuthorByName(string name)
        {
            return _context.Authors.FirstOrDefault(a => a.Name.Equals(name));
        }

        public Author GetAuthorById(int id)
        {
            return _context.Authors.Find(id);
        }

        public void AddAuthor(Author author)
        {
            _context.Authors.Add(author);
            _context.SaveChanges();
        }

        public void UpdateAuthor(Author author)
        {
            var entry = _context.Authors.Update(GetAuthorById(author.Id));

            if (entry != null)
            {
                EntryUpdater(entry, author);
            }
            else
            {
                AddAuthor(author);
            }
        }

        public void DeleteAuthor(int id)
        {
            var entry =_context.Authors.Remove(GetAuthorById(id));
            DeleteArticlesByAuthor(entry.Entity.Name);
            _context.SaveChanges();
        }
        #endregion
    }
}
