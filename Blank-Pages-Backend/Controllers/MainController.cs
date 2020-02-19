using Blank_Pages_Backend.Models;
using Microsoft.AspNetCore.Mvc;

namespace Blank_Pages_Backend.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class MainController : ControllerBase
    {
        private DataHandler _provider;
        private readonly Utilities _utils;

        public MainController(DataHandler provider, Utilities utils)
        {
            _provider = provider;
            utils.SetDbContext(_provider);
            _utils = utils;
        }

        #region Articles

        [HttpGet]
        public IActionResult GetMainPage()
        {
            return Ok();
        }

        //[HttpGet("articles/{id}")]
        //public async Task<ActionResult<Article>> GetArticleById(int id)
        //{
        //    return Ok();
        //}

        [HttpPut("/articles/{id}")]
        public IActionResult UpdateArticle(int id)
        {
            return Ok();
        }

        [HttpDelete("articles/{id}")]
        public IActionResult ArticleDelete(int id)
        {
            return Ok();
        }

        [HttpPost("articles/write")]
        public IActionResult AddNewArticle(Article article)
        {
            return Ok();
        }
        #endregion

        #region Search

        [HttpGet("/search")]
        public IActionResult GetSearchPage()
        {
            return Ok();
        }

        //[HttpGet("search/q?={searchPhrase}")]
        //public async Task<ActionResult<List<Article>>> GetArticlesWithPhrase(string phrase)
        //{
        //    return Ok();
        //}

        #endregion

        #region Authors

        [HttpPost("/authors/login")]
        public IActionResult LoginAuthor(Author author)
        {
            return Ok();
        }

        [HttpPost("/authors/register")]
        public IActionResult RegisterAuthor(Author author)
        {
            return Ok();
        }

        //[HttpGet("/authors/{id}")]
        //public Task<ActionResult<Author>> GetAuthorPage(int id)
        //{
        //    return Ok();
        //}

        [HttpPut("/authors/{id}")]
        public IActionResult UpdateAuthor(int id)
        {
            return Ok();
        }

        [HttpDelete("/authors/{id}")]
        public IActionResult DeleteAuthor(int id)
        {
            return Ok();
        }

        #endregion
    }
}
