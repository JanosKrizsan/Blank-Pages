using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    public class Utilities
    {
        private DataProvider _provider;

        #region General

        private const string _saveFilePath = @"C:\Users\Public\Documents\Articles\";
        public void SetDbContext(DataProvider provider)
        {
            _provider = provider;
        }

        #endregion

        #region Article Handling

        public Article GetArticle(int id)
        {
            return _provider.GetArticleById(id);
        }

        public List<int> GetArticleIds()
        {
            return _provider.GetAllArticleIds();
        }

        public List<Article> GetAllArticleData()
        {
            return _provider.GetAllArticles();
        }

        public Article ReadFromFile(int articleId)
        {
            var articlePath = _provider.GetArticleById(articleId).FilePath;

            var fileName = Path.GetFileName(articlePath);
            var saveFilePath = articlePath.Replace(fileName, "");
            var serializer = new XmlSerializer(typeof(Article));

            using var stream = new FileStream(string.Concat(saveFilePath, fileName), FileMode.Open, FileAccess.Read);
            var reader = new XmlTextReader(stream);
            return (Article)serializer.Deserialize(reader);
        }

        public void SaveToFile(Article article, bool update = false)
        {
            if (update)
            {
                article.CreationDate = DateTime.Now;
            }

            if (!Directory.Exists(_saveFilePath))
            {
                Directory.CreateDirectory(_saveFilePath);
            }

            var fileName = article.Title.Trim().Replace(" ", "-") + ".xml";
            article.FilePath = string.Concat(_saveFilePath, fileName);
            var serializer = new XmlSerializer(typeof(Article));

            using var writer = new StreamWriter(article.FilePath);
            serializer.Serialize(writer, article);

            if (update)
            {
                _provider.UpdateArticle(article);
            }
            else
            {
                _provider.AddArticle(article);
            }
        }

        public bool DoesArticleExist(string title)
        {
            return _provider.GetArticleByTitle(title) != null ? true : false;
        }

        public void DeleteArticle(int id)
        {
            var article = _provider.GetArticleById(id);
            var files = Directory.GetFiles(_saveFilePath).ToList();
            var file = files.FirstOrDefault(fl => Path.GetFullPath(fl).Equals(article.FilePath));

            if (!string.IsNullOrEmpty(file))
            {
                File.Delete(file);
                _provider.DeleteArticle(article);
            }

        }

        #endregion

        #region Source Handling

        public List<Source> GetAllSources()
        {
            return _provider.GetAllSources();
        }

        public Source GetSource(int id)
        {
            return _provider.GetSourceById(id);
        }

        public void AddSource(Source source)
        {
            _provider.AddSource(source);
        }

        public bool DoesSourceExist(string name)
        {
            return _provider.GetSourceByName(name) != null ? true : false;
        }

        public void UpdateSource(Source source)
        {
             _provider.UpdateSource(source);
        }

        public void RemoveSource(int id)
        {
            _provider.DeleteSourceById(id);
        }

        #endregion

        #region Search Handling

        public List<Article> SearchPhrase(string phrase)
        {
            return _provider.GetFilteredArticles(phrase);
        }

        #endregion

        #region Author Handling

        public bool IsAuthorized(string name, string pass)
        {
            return VerifyPassword(pass, name);
        }
        public Author GetAuthor(string name)
        {
            return _provider.GetAuthorByName(name);
        }

        public void AddAuthor(string name, string pass)
        {
            var author = new Author
            {
                Name = name,
                PassHash = HashPass(pass)
            };

            _provider.AddAuthor(author);
        }

        public void EditAuthor(string name, string pass, string newPass)
        {
            var author = _provider.GetAuthorByName(name);
            author.PassHash = HashPass(newPass);
            _provider.UpdateAuthor(author);
        }

        public void DeleteAuthor(int id)
        {
            _provider.DeleteAuthor(id);
        }

        public bool DoesAuthorExist(string name)
        {
            return _provider.GetAuthorByName(name) == null ? false : true;
        }

        public bool VerifyPassword(string password, string name)
        {
            var authorPass = _provider.GetAuthorByName(name).PassHash;
            return BCrypt.Net.BCrypt.Verify(password, authorPass);
        }

        public string HashPass(string password)
        {
            return BCrypt.Net.BCrypt.HashPassword(password);
        }

        #endregion
    }
}
