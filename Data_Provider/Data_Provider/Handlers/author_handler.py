"""
Handles author related queries.
"""

from .query_handler import Query_Handler as Queries
from Data_Provider.Static.utils import create_val_string, create_author, hash_n_salt_pass
import bcrypt

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

	def get_password(self, search_column, phrase):
		data = super().get_data("password", "authors", search_column, phrase)
		return data

	def update_data(self, values, search_column, phrase):
		pass_placement
		if "password" in values:
			for i, item in enumerate(values):
				if item == "password":
					pass_placement = values[i + 1]
					break
		password = values[pass_placement]
		values[pass_placement] = hash_n_salt_pass(password)
		super().update_data("authors", create_val_string(values), search_column, phrase)

	def add_data(self, values):
		vals = [values[0], hash_n_salt_pass(values[1])]
		super().add_data("authors", "name, password", values)

	def delete_data(self, phrase):
		super().delete_data("authors", "name", phrase)

	def wipe_data(self):
		super().wipe_data("authors")

	def check_connection(self):
		super().check_connection()
