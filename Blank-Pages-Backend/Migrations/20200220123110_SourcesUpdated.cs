using Microsoft.EntityFrameworkCore.Migrations;

namespace Blank_Pages_Backend.Migrations
{
    public partial class SourcesUpdated : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Sources_Articles_ArticleId",
                table: "Sources");

            migrationBuilder.DropPrimaryKey(
                name: "PK_Sources",
                table: "Sources");

            migrationBuilder.DropIndex(
                name: "IX_Sources_ArticleId",
                table: "Sources");

            migrationBuilder.DropColumn(
                name: "SourceId",
                table: "Sources");

            migrationBuilder.DropColumn(
                name: "ArticleId",
                table: "Sources");

            migrationBuilder.AddColumn<int>(
                name: "Id",
                table: "Sources",
                nullable: false,
                defaultValue: 0)
                .Annotation("SqlServer:Identity", "1, 1");

            migrationBuilder.AddColumn<int>(
                name: "ParentArticleId",
                table: "Sources",
                nullable: true);

            migrationBuilder.AddPrimaryKey(
                name: "PK_Sources",
                table: "Sources",
                column: "Id");

            migrationBuilder.CreateIndex(
                name: "IX_Sources_ParentArticleId",
                table: "Sources",
                column: "ParentArticleId");

            migrationBuilder.AddForeignKey(
                name: "FK_Sources_Articles_ParentArticleId",
                table: "Sources",
                column: "ParentArticleId",
                principalTable: "Articles",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Sources_Articles_ParentArticleId",
                table: "Sources");

            migrationBuilder.DropPrimaryKey(
                name: "PK_Sources",
                table: "Sources");

            migrationBuilder.DropIndex(
                name: "IX_Sources_ParentArticleId",
                table: "Sources");

            migrationBuilder.DropColumn(
                name: "Id",
                table: "Sources");

            migrationBuilder.DropColumn(
                name: "ParentArticleId",
                table: "Sources");

            migrationBuilder.AddColumn<int>(
                name: "SourceId",
                table: "Sources",
                type: "int",
                nullable: false,
                defaultValue: 0)
                .Annotation("SqlServer:Identity", "1, 1");

            migrationBuilder.AddColumn<int>(
                name: "ArticleId",
                table: "Sources",
                type: "int",
                nullable: true);

            migrationBuilder.AddPrimaryKey(
                name: "PK_Sources",
                table: "Sources",
                column: "SourceId");

            migrationBuilder.CreateIndex(
                name: "IX_Sources_ArticleId",
                table: "Sources",
                column: "ArticleId");

            migrationBuilder.AddForeignKey(
                name: "FK_Sources_Articles_ArticleId",
                table: "Sources",
                column: "ArticleId",
                principalTable: "Articles",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
