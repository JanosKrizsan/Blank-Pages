from Data_Provider.Models.author import Author
from Data_Provider.Models.article import Article
from Data_Provider.Models.source import Source


def create_val_string(values):
	string_vals = []
	for k, v in values:
		string_vals.append(f"{k} = {v}")
		if k != values.keys()[-1]:
			string_vals.append(", ")
		else:
			string_vals.append("")
	return "".join(string_vals)

def create_author(data):
	author = Author()
	return author

def create_article(data):
	article = Article()
	return article

def create_source(data):
	source = Source()
	return source

def serialize_to_file():
	pass

def read_from_file():
	pass
