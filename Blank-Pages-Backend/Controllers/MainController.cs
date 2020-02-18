using Blank_Pages_Backend.Data;
using Microsoft.AspNetCore.Mvc;

namespace Blank_Pages_Backend.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class MainController : ControllerBase
    {
        private BlankPagesDbContext _dbContext;
        public MainController(BlankPagesDbContext context)
        {
            _dbContext = context;
        }

        [HttpGet]
        public IActionResult Get()
        {
            
            return Ok(_dbContext.Articles);
        }



    }
}
