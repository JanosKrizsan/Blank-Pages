using Blank_Pages_Backend.Models;
using Microsoft.EntityFrameworkCore;

namespace Blank_Pages_Backend.Data
{
    public class BlankPagesDbContext : DbContext 
    {
        public DbSet<Article> Articles { get; set; }
        public DbSet<Author> Authors { get; set; }

        public BlankPagesDbContext(DbContextOptions<BlankPagesDbContext> options) : 
            base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.Entity<Author>()
                .HasIndex(i => i.Name)
                .IsUnique();
        }

    }
}
