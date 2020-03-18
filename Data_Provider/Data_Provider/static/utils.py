from Data_Provider.Models.author import Author
from Data_Provider.Models.article import Article
from Data_Provider.Models.source import Source
from flask import jsonify, json, make_response
from Data_Provider.Handlers import article_handler, author_handler, source_handler
from Data_Provider.Static.creds import psql_creds
import datetime
import xml.etree.ElementTree as et
import io

authors = author_handler.Author_Handler(creds[0], creds[1], creds[2])
articles = article_handler.Article_Handler(creds[0], creds[1], creds[2])
sources = source_handler.Source_Handler(creds[0], creds[1], creds[2])

def response_creator(stat_code, resp_string, obj = None):
	pass

def get_req_handler(table, mass_dat, phrase, search_col ):
	auth = authors.get_all_data if mass_dat else authors.get_data
	arti = articles.get_all_data if mass_dat else articles.get_data
	sour = sources.get_all_data if mass_dat else sources.get_data
	switcher = {
		'au' : auth,
		'ar' : arti,
		'sr' : sour
		}
	func = switcher.get(table, None)
	if func != None:
		if mass_dat:
			return func()
		else:
			return func(search_col, phrase)
	else:
		return AttributeError("Invalid Data Provided")

def post_req_handler(table, vals):
	func = authors.add_data if table == 'au' else articles.add_data if table == 'ar' else sources.add_data if table == 'sr' else None
	if func == None:
		return AttributeError("Invalid Data Provided")
	func(vals)
	return True

def put_req_handler(table, vals, col, phrase,):
	func = authors.update_data if table == 'au' else articles.update_data if table == 'ar' else sources.update_data if table == 'sr' else None
	if func == None:
		return AttributeError("Invalid Data Provided")
	func(vals, col, phrase)
	return True

def del_req_handler(table, mass_dat, phrase):
	auth = authors.wipe_data if mass_dat else authors.delete_data
	arti = articles.wipe_data if mass_dat else articles.delete_data
	sour = sources.wipe_data if mass_dat else sources.delete_data
	switcher = {
		'au' : auth,
		'ar' : arti,
		'sr' : sour
		}
	func = switcher.get(table, None)
	if func != None:
		if mass_dat:
			func()
		else:
			func(phrase)
			return True
	else:
		return AttributeError("Invalid Data Provided")

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
