from .query_handler import Query_Handler as Queries

class Article_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super(Article_Handler, self).__init__(name, pwd, db)

	def GetData():
		return super(Article_Handler, self).GetData()

	def GetAllData():
		return super(Article_Handler, self).GetAllData()

	def UpdateData():
		return super(Article_Handler, self).UpdateData()

	def UpdateBulkData():
		return super(Article_Handler, self).UpdateBulkData()

	def DeleteData():
		return super(Article_Handler, self).DeleteData()

	def WipeData():
		return super(Article_Handler, self).WipeData()