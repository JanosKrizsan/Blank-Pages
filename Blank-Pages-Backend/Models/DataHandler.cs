using Blank_Pages_Backend.Data;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Blank_Pages_Backend.Models
{
    public class DataHandler
    {
        private BlankPagesDbContext _context;

        #region General

        public DataHandler(BlankPagesDbContext dbcontext)
        {
            _context = dbcontext;
        }

        private void EntryUpdater(EntityEntry entry, object updatedEntry)
        {
            dynamic update = null;
            if (updatedEntry is Article)
            {
                update = (Article)updatedEntry;
            }
            else
            {
                update = (Author)updatedEntry;
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

        public Article GetArticleById(int id)
        {
            return _context.Articles.Find(id);
        }

        public List<Article> GetArticlesByAuthor(string authorName)
        {
            return _context.Authors.Where(a => a.Name.Equals(authorName)).Select(a => a.ArticlesWritten.ToList()).FirstOrDefault(list => list is List<Article>);
        }

        public void AddArticle(Article article)
        {
            _context.Articles.Add(article);
            _context.SaveChanges();
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
            _context.Authors.Remove(GetAuthorById(id));
            _context.SaveChanges();
        }
        #endregion
    }
}
