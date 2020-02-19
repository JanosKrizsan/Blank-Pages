using Blank_Pages_Backend.Data;
using System.IO;
using System.Xml;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    public class Utilities
    {
        private DataHandler _provider;

        #region General

        public void SetDbContext(DataHandler provider)
        {
            _provider = provider;
        }

        #endregion

        #region Article Handling
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

        public void SaveToFile(Article article)
        {
            var saveFilePath = @"C:\Users\Public\Documents\Articles";
            var fileName = article.Title.Trim().Replace(" ", "-") + ".xml";
            var serializer = new XmlSerializer(typeof(Article));

            using var writer = new StreamWriter(string.Concat(saveFilePath, fileName));
            serializer.Serialize(writer, article);
        }

        #endregion

        #region Author Handling

        public bool VerifyPassword(string password, Author author)
        {
            var authorPass = _provider.GetAuthorByName(author.Name).PassHash;
            return BCrypt.Net.BCrypt.Verify(password, authorPass);
        }

        public string HashPass(string password)
        {
            return BCrypt.Net.BCrypt.HashPassword(password);
        }
        #endregion
    }
}
