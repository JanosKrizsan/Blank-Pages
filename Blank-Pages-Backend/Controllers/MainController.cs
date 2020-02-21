using Blank_Pages_Backend.Models;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace Blank_Pages_Backend.Controllers
{

    [ApiController]
    [Route("[controller]")]
    public class MainController : ControllerBase
    {
        #region General
        private readonly Utilities _utils;
        private readonly string _main = "main/";
        private readonly string _unauthorized = "Access Not Authorized";

        public MainController(DataProvider provider, Utilities utils)
        {
            utils.SetDbContext(provider);
            _utils = utils;
        }

        #endregion

        #region Articles

        [HttpGet]
        public ActionResult<List<Article>> GetMainPage()
        {
            var articles = _utils.GetArticleIds();

            if (articles.Count != 0)
            {
                var contentData = new List<Article>();
                articles.ForEach(id => contentData.Add(_utils.ReadFromFile(id)));
                return Ok(contentData);
            }

            return NoContent();
        }

        [HttpGet("articles/")]
        public ActionResult<List<Article>> GetArticlesPage()
        {
            var articles =_utils.GetAllArticleData();
            if (articles.Count != 0)
            {
                return Ok(articles);
            }
            return NoContent();
           
        }
        [HttpGet("articles/{id}")]
        public ActionResult<Article> GetArticleById([FromRoute] int id)
        {
            var article = _utils.GetArticle(id);

            if (article != null)
            {
                article.Content = _utils.ReadFromFile(id).Content;
                return Ok(article);
            }

            return NotFound();
        }

        [HttpPut("articles/{id}")]
        public IActionResult UpdateArticle([FromBody] Article article)
        {
            _utils.SaveToFile(article, true);
            return Ok("Successful Article Update");
        }

        [HttpDelete("articles/{id}")]
        public IActionResult ArticleDelete([FromRoute] int id)
        {
            _utils.DeleteArticle(id);
            return Redirect(_main);
        }

        [HttpPost("articles/write")]
        public IActionResult AddNewArticle(Article article)
        {
            if (_utils.DoesArticleExist(article.Title))
            {
                return Conflict("Article Exists");
            }
            _utils.SaveToFile(article);
            return Ok("Successful Article Save");
        }

        #endregion

        #region Sources

        [HttpGet("sources/")]
        public ActionResult<List<Source>> GetSourcesPage()
        {
            var sources = _utils.GetAllSources();
            if(sources.Count == 0)
            {
                return Redirect("sources/add");
            }
            return Ok(sources);
        }

        [HttpGet("sources/{id}")]
        public ActionResult<Source> GetSourceInfo([FromRoute] int id)
        {
            var source = _utils.GetSource(id);
            if (source == null)
            {
                return NotFound();
            }
            return Ok(source);
        }
        
        [HttpDelete("sources/{id}")]
        public IActionResult DeleteSource([FromRoute] int id)
        {
            _utils.RemoveSource(id);
            return Redirect("sources/");
        }

        [HttpPost("sources/add")]
        public IActionResult AddSource([FromBody] Source source)
        {
            if (_utils.DoesSourceExist(source.Name))
            {
                return Conflict("Source Exists");
            }
            _utils.AddSource(source);
            return Ok("Successful Source Addition");
        }

        [HttpPut("sources/{id}")]
        public IActionResult UpdateSourceInfo([FromBody] Source source)
        {
            _utils.UpdateSource(source);
            return Ok("Succesful Source Update");
        }

        #endregion

        #region Search

        [HttpPost("search/q={searchPhrase}")]
        public ActionResult<List<Article>> GetArticlesWithPhrase([FromRoute] string searchPhrase)
        {
            var articles = _utils.SearchPhrase(searchPhrase);

            if (articles.Count != 0)
            {
                return Ok(articles);
            }
            return NoContent();
        }

        #endregion

        #region Authors

        [HttpPost("authors/login")]
        public IActionResult LoginAuthor([FromBody] AuthorDto author)
        {
            if (_utils.DoesAuthorExist(author.Name))
            {
                return _utils.IsAuthorized(author.Name, author.Pass) ? Ok("Successful Login") : ValidationProblem("Password Or Username Invalid");
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpPost("authors/register")]
        public IActionResult RegisterAuthor([FromBody] AuthorDto author)
        {
            if (!_utils.DoesAuthorExist(author.Name))
            {
                _utils.AddAuthor(author.Name, author.Pass);
                return Ok("Successful Registration");
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpPut("authors/{id}")]
        public IActionResult UpdateAuthor([FromBody] AuthorDto author)
        {
            if (_utils.IsAuthorized(author.Name, author.Pass))
            {
                _utils.EditAuthor(author.Name, author.Pass, author.NewPass);
                return Ok("Successful Password Update");
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpDelete("authors/{id}")]
        public IActionResult DeleteAuthor([FromRoute] int id, [FromBody] AuthorDto author)
        {
            if (_utils.IsAuthorized(author.Name, author.Pass))
            {
                _utils.DeleteAuthor(id);
                return Redirect("main/");
            }
            return ValidationProblem(_unauthorized);
        }

        #endregion
    }
}
