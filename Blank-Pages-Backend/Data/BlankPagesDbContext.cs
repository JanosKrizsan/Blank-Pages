using Blank_Pages_Backend.Models;
using Microsoft.EntityFrameworkCore;

namespace Blank_Pages_Backend.Data
{
    public class BlankPagesDbContext : DbContext 
    {
        public DbSet<Article> Articles { get; set; }
        public DbSet<Author> Authors { get; set; }

        public DbSet<Source> Sources { get; set; }

        public BlankPagesDbContext(DbContextOptions<BlankPagesDbContext> options) : 
            base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.Entity<Author>()
                .HasIndex(i => i.Name)
                .IsUnique();

            builder.Entity<Author>()
                .HasMany(art => art.ArticlesWritten)    
                .WithOne(a => a.ArticleAuthor);

            builder.Entity<Article>()
                .HasIndex(i => i.Title)
                .IsUnique();

            builder.Entity<Article>()
                .HasMany(i => i.Sources)
                .WithOne(s => s.ParentArticle);

        }

    }
}
