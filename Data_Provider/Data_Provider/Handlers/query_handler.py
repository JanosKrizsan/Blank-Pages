from Data_Provider.Handlers.connection_handler import Connection_Handler as conn
import abc

class Query_Handler(object, metaclass=abc.ABCMeta):

	def __init__(self, name = "postgres", pwd = "postgres", db = "blank_pages_db"):
		self.conn = conn(name, pwd, db)
		self.conn.check_database_exists()

	@abc.abstractmethod
	def GetData():
		raise NotImplementedError("You must implement this method!")

	@abc.abstractmethod
	def GetAllData():
		raise NotImplementedError("You must implement this method!")

	@abc.abstractmethod
	def UpdateData():
		raise NotImplementedError("You must implement this method!")

	@abc.abstractmethod
	def UpdateBulkData():
		raise NotImplementedError("You must implement this method!")

	@abc.abstractmethod
	def DeleteData():
		raise NotImplementedError("You must implement this method!")

	@abc.abstractmethod
	def WipeData():
		raise NotImplementedError("You must implement this method!")
