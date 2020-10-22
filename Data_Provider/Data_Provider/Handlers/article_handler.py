"""
Handles article related queries.
"""

from .query_handler import Query_Handler as Queries
from Data_Provider.Statics.utils import create_val_string, create_article, serialize_to_file, read_from_file

class Article_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)

	def get_data(self, search_column, phrase):
		#TODO -> content info must be retrieved from XML file
		fields = ["title", "sub_title", "full_file_path", "author_id", "creation_date"]
		data = super().get_data(fields, "articles", search_column, phrase)
		return create_article(data)

	def get_all_data(self):
		#TODO -> content info must be retrieved from XML files
		datas = super().get_all_data("articles")
		articles = []
		for dat in datas:
			articles.append(create_article(dat))
		return articles

	def update_data(self, values, search_column, phrase):
		#TODO -> make sure the data is saved to XML here
		super().update_data("articles", create_val_string(values), search_column, phrase)

	def add_data(self, values):
		#TODO -> make sure the data is saved to XML here
		columns = ["title", "sub_title", "full_file_path", "author_id", "creation_date"]
		super().add_data("articles", columns, values)

	def delete_data(self, search_column, phrase):
		super().delete_data("articles", search_column, phrase)

	def wipe_data(self):
		super().wipe_data("articles")
