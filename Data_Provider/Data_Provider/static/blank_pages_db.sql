DROP TABLE IF EXISTS dbo.Authors;
DROP TABLE IF EXISTS dbo.Articles;
DROP TABLE IF EXISTS dbo.Sources;

CREATE TABLE Authors (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL UNIQUE,
	password VARCHAR(200) NOT NULL
);

CREATE TABLE Articles (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL UNIQUE,
	sub_title VARCHAR(40),
	full_file_path VARCHAR(255),
	author_id int NOT NULL,
	creation_date TIMESTAMP NOT NULL,
	FOREIGN KEY(author_id) REFERENCES Authors(id)
);

CREATE TABLE Sources (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL UNIQUE,
	source_data VARCHAR(100) NOT NULL,
	parent_article_id int,
	FOREIGN KEY(parent_article_id) REFERENCES Articles(id)
);