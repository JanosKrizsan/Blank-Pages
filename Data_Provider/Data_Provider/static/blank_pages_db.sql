CREATE TABLE blank_pages.authors (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL UNIQUE,
	password VARCHAR(100) NOT NULL
);

CREATE TABLE blank_pages.articles (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL UNIQUE,
	sub_title VARCHAR(40),
	full_file_path VARCHAR(255),
	author_id int NOT NULL,
	creation_date TIMESTAMP NOT NULL,
	FOREIGN KEY(author_id) REFERENCES blank_pages.authors(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE blank_pages.sources (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL UNIQUE,
	source_data VARCHAR(100) NOT NULL,
	parent_article_id int,
	FOREIGN KEY(parent_article_id) REFERENCES blank_pages.articles(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE blank_pages.blacklist (
	id SERIAL PRIMARY KEY,
	address INET NOT NULL UNIQUE,
	author_id int, 
	FOREIGN KEY(author_id) REFERENCES blank_pages.authors(id) ON DELETE CASCADE ON UPDATE CASCADE
);