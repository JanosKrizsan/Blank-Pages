using System;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    [XmlRoot("SrcInfo")]
    public class Source : IComparable
    {
        [XmlElement("SrcId")]
        public int Id { get; set; }
        
        [XmlElement("SrcName")]
        public string Name { get; set; }
        
        [XmlElement("SrcData")]
        public string SourceData { get; set; }

        [XmlIgnore]
        public Article ParentArticle { get; set; }

        public int CompareTo(object otherSource)
        {
            var other = (Source)otherSource;
            return Id > other.Id ? 1 : -1;
        }
    }
}
