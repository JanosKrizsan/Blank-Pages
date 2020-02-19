using Blank_Pages_Backend.Data;

namespace Blank_Pages_Backend.Models
{
    public class DataProvider
    {
        private BlankPagesDbContext _context;

        public DataProvider(BlankPagesDbContext dbcontext)
        {
            _context = dbcontext;
        }

        public Article GetArticleById(int id)
        {
            return _context.Articles.Find(id);
        }

        public 
    }
}
