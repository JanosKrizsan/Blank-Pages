using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blank_Pages_Backend.Models
{
    public class Article
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string SubTitle { get; set; }
        public string FilePath { get; set; }
        public string Author { get; set; }
    }
}
