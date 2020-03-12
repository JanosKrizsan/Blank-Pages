from .query_handler import Query_Handler as Queries
from Data_Provider.Models.author import Author as auth
from Data_Provider.Static.utils import create_val_string

class Author_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super().__init__(name, pwd, db)

	def GetData(phrase):
		fields = "id, name, password"
		data = super().GetData(fields, "authors", "name", phrase)
		author = auth()
		return author

	def GetAllData():
		data = super().GetAllData("authors")
		return data

	def UpdateData(values, search_column, phrase):
		super().UpdateData("authors", create_val_string(values), search_column, phrase)

	def AddData(values):
		super().AddData("authors", "name, password", values)

	def DeleteData(phrase):
		super().DeleteData("authors", "name", phrase)

	def WipeData():
		super().WipeData("authors")
