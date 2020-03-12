from .query_handler import Query_Handler as Queries
from Data_Provider.Models.source import Source as src
from Data_Provider.Static.utils import create_val_string

class Source_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)
	
	def GetData(search_column, phrase):
		fields = "name, source_data, parent_article_id"
		data = super().GetData(fields, "sources", search_column, phrase)

	def GetAllData():
		return super().GetAllData("sources")

	def UpdateData(values, search_column, phrase):
		super().UpdateData("sources", create_val_string(values), search_column, phrase)

	def AddData(values):
		super().AddData("sources", "name, source_data, parent_article_id", values)

	def DeleteData(search_column, phrase):
		super().DeleteData("sources", search_column, phrase)

	def WipeData():
		super().WipeData("sources")
