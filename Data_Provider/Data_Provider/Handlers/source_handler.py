from .query_handler import Query_Handler as Queries
from Data_Provider.Models.source import Source as src
from Data_Provider.Static.utils import create_val_string, create_source

class Source_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)
	
	def get_data(self, search_column, phrase):
		fields = "name, source_data, parent_article_id"
		data = super().get_data(fields, "sources", search_column, phrase)
		return create_source(data)

	def get_all_data(self):
		datas = super().get_all_data("sources")
		sources = []
		for dat in datas:
			sources.append(create_source(dat))
		return sources

	def update_data(self, values, search_column, phrase):
		super().update_data("sources", create_val_string(values), search_column, phrase)

	def add_data(self, values):
		super().add_data("sources", "name, source_data, parent_article_id", values)

	def delete_data(self, search_column, phrase):
		super().delete_data("sources", search_column, phrase)

	def wipe_data(self):
		super().wipe_data("sources")
