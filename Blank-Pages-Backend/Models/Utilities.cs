using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Serialization;

namespace Blank_Pages_Backend.Models
{
    public class Utilities
    {
        public Article ReadFromFile()
        {
            var saveFilePath = "";
            var fileName = "";
            var serializer = new XmlSerializer(typeof(Article));

            using var stream = new FileStream(string.Concat(saveFilePath, fileName), FileMode.Open, FileAccess.Read);
            var reader = new XmlTextReader(stream);
            return (Article)serializer.Deserialize(reader);
        }

        public void SaveToFile()
        {

        }
    }
}
