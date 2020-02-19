using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Blank_Pages_Backend.Models
{
    public class Author
    {
        public int Id { get; set; }

        [MinLength(4, ErrorMessage = "Author name must be longer than 4 characters.")]
        [MaxLength(8, ErrorMessage = "Author name cannot be longer than 8 characters.")]
        public string Name { get; set; }

        public string PassHash { get; set; }

        public ICollection<Article> ArticlesWritten { get; set; }
    }
}
