using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    [XmlRoot("Article")]
    public class Article : IComparable
    {
        [XmlElement("ArticleID")]
        public int Id { get; set; }

        [XmlElement("Title")]
        public string Title { get; set; }

        [XmlElement("SubTitle")]
        public string SubTitle { get; set; }

        [XmlElement("Content")]
        [NotMapped]
        public string Content { get; set; }

        [XmlElement("FullFilePath")]
        public string FilePath { get; set; }

        [XmlElement("Author")]
        public Author ArticleAuthor { get; set; }
        
        [XmlElement("CreationDate")]
        public DateTime CreationDate { get; set; }

        [XmlElement("Sources")]
        public IList<Source> Sources { get; set; }
        public int CompareTo(object otherArticle)
        {
            var other = (Article)otherArticle;
            return Id > other.Id ? 1 : -1;
        }
    }
}
