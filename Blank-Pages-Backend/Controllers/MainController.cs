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

            if (articles != null)
            {
                var contentData = new List<Article>();
                articles.ForEach(id => contentData.Add(_utils.ReadFromFile(id)));
                return Ok(contentData);
            }

            return NoContent();
        }

        [HttpGet("articles/{id}")]
        public ActionResult<Article> GetArticleById(int id)
        {
            var article = _utils.GetArticle(id);

            if (article != null)
            {
                article.Content = _utils.ReadFromFile(id).Content;
                return Ok(article);
            }

            return NotFound();
        }

        [HttpPut("/articles/{id}")]
        public IActionResult UpdateArticle(Article article)
        {
            _utils.SaveToFile(article, true);
            return Ok("Successful Article Update");
        }

        [HttpDelete("articles/{id}")]
        public IActionResult ArticleDelete(Article article)
        {
            _utils.DeleteArticle(article);
            return Redirect(_main);
        }

        [HttpPost("articles/write")]
        public IActionResult AddNewArticle(Article article)
        {
            _utils.SaveToFile(article);
            return Ok("Successful Article Save");
        }

        #endregion

        #region Sources

        [HttpGet("sources/")]
        public ActionResult<List<Source>> GetSourcesPage()
        {
            var sources = _utils.GetAllSources();
            if(sources == null)
            {
                return Redirect("sources/add");
            }
            return Ok(sources);
        }

        [HttpGet("sources/{id}")]
        public ActionResult<Source> GetSourceInfo(int id)
        {
            var source = _utils.GetSource(id);
            if (source == null)
            {
                return NotFound();
            }
            return Ok(source);
        }


        [HttpDelete("sources/{id}")]
        public ActionResult DeleteSource(int id)
        {
            _utils.RemoveSource(id);
            return Redirect("sources/");
        }

        [HttpPost("sources/add")]
        public ActionResult AddSource(Source source)
        {
            _utils.AddSource(source);
            return Ok("Successful Source Addition");
        }

        [HttpPut("sources/{id}")]
        public ActionResult<Source> UpdateSourceInfo(Source source)
        {
            _utils.UpdateSource(source);
            return Ok("Succesful Source Update");
        }

        #endregion

        #region Search

        [HttpPost("search/q?={searchPhrase}")]
        public ActionResult<List<Article>> GetArticlesWithPhrase(string phrase)
        {
            var articles = _utils.SearchPhrase(phrase);

            if (articles != null)
            {
                return Ok(articles);
            }
            return NoContent();
        }

        #endregion

        #region Authors

        [HttpPost("/authors/login")]
        public IActionResult LoginAuthor(string name, string pass)
        {
            if (!_utils.DoesAuthorExist(name))
            {
                return _utils.IsAuthorized(name, pass) ? Ok("Successful Login") : ValidationProblem();
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpPost("/authors/register")]
        public IActionResult RegisterAuthor(string name, string pass)
        {
            if (!_utils.DoesAuthorExist(name))
            {
                _utils.AddAuthor(name, pass);
                return Ok("Successful Registration");
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpPut("/authors/{id}")]
        public IActionResult UpdateAuthor(string name, string pass, string newPass)
        {
            if (_utils.IsAuthorized(name, pass))
            {
                _utils.EditAuthor(name, pass, newPass);
                return Ok("Successful Password Update");
            }
            return ValidationProblem(_unauthorized);
        }

        [HttpDelete("/authors/{id}")]
        public IActionResult DeleteAuthor(int id, string name, string pass)
        {
            if (_utils.IsAuthorized(name, pass))
            {
                _utils.DeleteAuthor(id);
                return Redirect("main/");
            }
            return ValidationProblem(_unauthorized);
        }

        #endregion
    }
}
