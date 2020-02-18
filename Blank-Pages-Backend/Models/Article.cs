using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    [XmlRoot("Article")]
    public class Article
    {
        [XmlElement("ArticleID")]
        public int Id { get; set; }

        [XmlElement("Title")]
        public string Title { get; set; }

        [XmlElement("SubTitle")]
        public string SubTitle { get; set; }

        [XmlElement("Content")]
        public string Content { get; set; }

        [XmlElement("FullFilePath")]
        public string FilePath { get; set; }

        [XmlElement("ArticleAuthor")]
        public int AuthorId { get; set; }
    }
}
