"""
Handles author related queries.
"""

from .query_handler import Query_Handler as Queries
from Data_Provider.Models.author import Author as auth
from Data_Provider.Static.utils import create_val_string, create_author

class Author_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)

	def get_data(self, search_column, phrase):
		fields = "id, name"
		data = super().get_data(fields, "authors", search_column, phrase)
		return create_author(data)

	def get_all_data(self):
		datas = super().get_all_data("authors")
		authors = []
		for dat in datas:
			authors.append(create_author(dat))
		return authors

	def update_data(self, values, search_column, phrase):
		super().update_data("authors", create_val_string(values), search_column, phrase)

	def add_data(self, values):
		super().add_data("authors", "name, password", values)

	def delete_data(self, phrase):
		super().delete_data("authors", "name", phrase)

	def wipe_data(self):
		super().wipe_data("authors")

	def check_connection(self):
		super().check_connection()
		return True
