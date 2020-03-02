from Data_Provider.Handlers.connection_handler import Connection_Handler as conn

class Query_Handler(object):

	def __init__(self):
		self.conn = conn("john", "1710", "blank_pages_db")
		self.conn.check_database_exists()


