from .query_handler import Query_Handler as Queries

class Author_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super(Author_Handler, self).__init__(name, pwd, db)

	def GetData():
		return super(Author_Handler, self).GetData()

	def GetAllData():
		return super(Author_Handler, self).GetAllData()

	def UpdateData():
		return super(Author_Handler, self).UpdateData()

	def UpdateBulkData():
		return super(Author_Handler, self).UpdateBulkData()

	def DeleteData():
		return super(Author_Handler, self).DeleteData()

	def WipeData():
		return super(Author_Handler, self).WipeData()
