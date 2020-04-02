"""
Object instantiation, saving/ reading articles to and fro' XML files.
"""

from Data_Provider.Models.author import Author
from Data_Provider.Models.article import Article
from Data_Provider.Models.source import Source
from Data_Provider.Models.address import Address
import datetime
import bcrypt
import xml.etree.ElementTree as et
import io

def hash_n_salt_pass(password):
	return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_hash_n_pass(hash, password):
	return hash == hash_n_salt_pass(password).decode("utf-8")

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

def create_address(data):
	address = Address()
	return setset_attributes(address, data)

def serialize_to_file(article):
	data = et.Element("article")
	title = et.SubElement(data, "title")
	sub_title = et.SubElement(data, "sub_title")
	content = et.SubElement(data, "content")
	author = et.SubElement(data, "author")
	creation_date = et.SubElement(data, "creation_date")
	sources = et.SubElement(data, "sources")
	
	title.text(f"{article.prop_name}")
	sub_title.text(f"{article.prop_sub_title}")
	content.text(f"{article.prop_content}")
	author.text(f"{article.prop_author_id}")
	creation_date.text(f"{article.prop_creation_date}")
	sources.text(f"{article.prop_sources}")
	
	article_data = et.tostring(data)
	with open(f"{article.prop_full_file_path}", "w") as article_file:
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
