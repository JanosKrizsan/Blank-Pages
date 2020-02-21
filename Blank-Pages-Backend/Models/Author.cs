using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    [XmlRoot("Author")]
    public class Author
    {
        [XmlElement("AuthorId")]
        public int Id { get; set; }

        [XmlElement("AuthorName")]
        [MinLength(4, ErrorMessage = "Author name must be longer than 4 characters.")]
        [MaxLength(8, ErrorMessage = "Author name cannot be longer than 8 characters.")]
        public string Name { get; set; }

        [XmlIgnore]
        public string PassHash { get; set; }

        [XmlIgnore]
        public List<Article> ArticlesWritten { get; set; }
    }
}
