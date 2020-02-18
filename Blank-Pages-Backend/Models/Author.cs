using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blank_Pages_Backend.Models
{
    public class Author
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string PassHash { get; set; }
        public ICollection<Article> ArticlesWritten { get; set; }
    }
}
