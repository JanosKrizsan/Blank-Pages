import psycopg2
import psycopg2.extras

class Connection_Handler(object):

	def __init__(self, user, password, db_name, address = None):
		self.user_name = user
		self.host_add = "localhost" if address == None else address
		self.password = password
		self.db = db_name
		self.conn_string = f"postgresql://{user}:{password}@{address}/{db_name}"

	def check_database_exists(self):
		connection = None
		try:
			connection = psycopg2.connect("user='postgres' host='localhost' password='postgres' port='5432'")
		except:
			print("Unable to connect to basic user.")
		if connection is not None:
			cursor = connection.cursor()
			cursor.execute("SELECT datname FROM pg_database")
			databases = cursor.fetchall()
			if self.db in databases:
				self.read_sql_from_file()
			else:
				self.create_database("blank_pages_db")
		else:
			print("PSQL could not be reached.")


	def connect_to_db(self):
		try:
			self.con = psycopg2.connect(self.conn_string)
			self.con.autocommit = True
			return self.con()
		except (Exception, psycopg2.DatabaseError) as error:
			print("Database does not exist, or another error occurred", error)


	def create_database(self, db_name = self.db):
		name = self.db if db_name == None else db_name
		connect_to_db().cursor().execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))

	def read_sql_from_file(self, file):
		connect_to_db().cursor().execute(open(self.file_path, r).read())


	def handler(function):
		def wrapper(*args, **kwargs):
			con = self.connect_to_db()
			dict_cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			ret_value = function(dict_cur, *args, **kwargs)
			dict_cur.close()
			self.con.close()
			return ret_value
		return wrapper

