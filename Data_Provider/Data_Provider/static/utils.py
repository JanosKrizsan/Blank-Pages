from Data_Provider.Models.author import Author
from Data_Provider.Models.article import Article
from Data_Provider.Models.source import Source
import datetime
import xml.etree.ElementTree as et
import io

def create_val_string(values):
	string_vals = []
	for k, v in values:
		string_vals.append(f"{k} = {v}")
		if k != values.keys()[-1]:
			string_vals.append(", ")
		else:
			string_vals.append("")
	return "".join(string_vals)


def set_attributes(obj, data):
	for k, v in data.items():
		setattr(obj, k, v)
	return obj

def create_author(data):
	author = Author()
	return set_attributes(author, data)

def create_article(data):
	article = Article()
	return set_attributes(article, data)

def create_source(data):
	source = Source()
	return set_attributes(source, data)

def serialize_to_file(article):
	data = et.Element("article")
	title = et.SubElement(data, "title")
	sub_title = et.SubElement(data, "sub_title")
	content = et.SubElement(data, "content")
	author = et.SubElement(data, "author")
	creation_date = et.SubElement(data, "creation_date")
	sources = et.SubElement(data, "sources")
	
	title.text(f"{article.prop_name}")
	sub_title.text(f"{article.prop_subtitle}")
	content.text(f"{article.prop_content}")
	author.text(f"{article.prop_author}")
	creation_date.text(f"{article.prop_creationdate}")
	sources.text(f"{article.prop_sources}")
	
	article_data = et.tostring(data)
	with open(f"{article.prop_fullfilepath}", "w") as article_file:
		article_file.write(article_data)


def read_from_file(file_path):
	data = et.parse(file_path)
	n = None
	article_info = {"prop_name" : data.findtext("title", n),
					"prop_subtitle" : data.findtext("sub_title", n),
					"prop_content" : data.findtext("content", n),
					"prop_author" : data.findtext("author", n),
					"prop_creationdate" : datetime.strptime(data.findtext("creation_date", n), "%m-%d-%Y").date(),
					"prop_sources" : data.findtext("sources", n)
					}
	return create_article(article_info)
