from Data_Provider.Static.utils import create_address
from .query_handler import Query_Handler as Queries

class Blacklist_Handler(Queries):

	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)

	def get_data(self, search_column, phrase):
		fields = "address, author_id"
		data = super().get_data(fields, "blacklist", search_column, phrase)
		return create_address(data)

	def add_data(self, values):
		columns = "address, author_id" if len(values) == 2 else "address"
		super().add_data("blacklist", columns, values)

	def delete_data(self, phrase):
		column = "author_id" if len(phrase) > 1 else "address"
		super().delete_data("blacklist", column, phrase)