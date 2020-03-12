from .query_handler import Query_Handler as Queries
from Data_Provider.Models.article import Article as arty
from Data_Provider.Static.utils import create_val_string

class Article_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)

	def GetData(search_column, phrase):
		fields = "title, sub_title, full_file_path, author_id, creation_date"
		data = super().GetData(fields, "articles", search_column, phrase)

	def GetAllData():
		return super().GetAllData("articles")

	def UpdateData(values, search_column, phrase):
		super().UpdateData("articles", create_val_string(values), search_column, phrase)

	def AddData(values):
		columns = "title, sub_title, full_file_path, author_id, creation_date"
		super().AddData("articles", columns, values)

	def DeleteData(search_column, phrase):
		super().DeleteData("articles", search_column, phrase)

	def WipeData():
		super().WipeData("articles")