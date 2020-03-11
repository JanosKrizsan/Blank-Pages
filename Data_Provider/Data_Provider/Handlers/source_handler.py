from .query_handler import Query_Handler as Queries

class Source_Handler(Queries):
	
	def __init__(self, name, pwd, db):
		super(Source_Handler, self).__init__(name, pwd, db)

	def GetData():
		return super(Source_Handler, self).GetData()

	def GetAllData():
		return super(Source_Handler, self).GetAllData()

	def UpdateData():
		return super(Source_Handler, self).UpdateData()

	def UpdateBulkData():
		return super(Source_Handler, self).UpdateBulkData()

	def DeleteData():
		return super(Source_Handler, self).DeleteData()

	def WipeData():
		return super(Source_Handler, self).WipeData()
