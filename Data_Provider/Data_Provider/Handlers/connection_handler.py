import psycopg2
import psycopg2.extras
import itertools
import io
import os
from psycopg2 import sql

class Connection_Handler(object):

	def __init__(self, user, password, db_name, address = None):
		self.user_name = user
		self.host_add = "localhost" if address == None else address
		self.password = password
		self.db = db_name
		self.conn_string = f"postgresql://{self.user_name}:{self.password}@{self.host_add}/{self.db}"
		self.file_path = self.get_relative_path() + "\\blank_pages_db.sql"

	def check_database_exists(self):
		self.conn = None
		try:
			self.conn = psycopg2.connect(host="localhost", user="postgres", password="postgres", port="5432")
		except (Exception, psycopg2.DatabaseError) as error:
			print("Unable to connect to database server.", error)
		if self.conn is not None:
			self.conn.autocommit = True
			curs = self.conn.cursor()
			curs.execute("SELECT datname FROM pg_database")
			databases = curs.fetchall()
			dbs = list(itertools.chain(*databases))
			if self.db in dbs:
				#This always returns false in python, but true in PSQL
				#TODO \\ ask about this
				curs.execute(sql.SQL("""
					SELECT EXISTS (
						SELECT FROM pg_catalog.pg_class c
						JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace
						WHERE  n.nspname = '{datbase}'
						AND    c.relname = 'authors'
						);
				""").format(datbase = sql.Identifier(self.db)))
				exists = curs.fetchone()[0]
				#if exists == False:
				#	self.read_sql_from_file()
			else:
				self.create_database(self.db)
		else:
			print("PSQL Database Provider could not be reached.")


	def connect_to_db(self):
		try:
			con = psycopg2.connect(self.conn_string)
			con.autocommit = True
		except (Exception, psycopg2.DatabaseError) as error:
			print("Database does not exist, or another error occurred:", error)
		return con


	def create_database(self, db_name = None):
		name = self.db if db_name == None else db_name
		self.conn = psycopg2.connect(host="localhost", user="postgres", password="postgres", port="5432")
		self.conn.autocommit = True
		self.conn.cursor().execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
		self.close_connections()


	def close_connections(self):
		self.conn.cursor().close()
		self.conn.close()


	def read_sql_from_file(self):
		conn = self.connect_to_db()
		conn.cursor().execute(open(self.file_path, 'r').read())
		self.close_connections()

	def get_relative_path(self):
		base = None
		dirs =[dir for dir in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(dir)]
		for d in dirs:
			if "Static" in os.listdir(d):
				base = os.path.abspath(d) + "\Static"
				break
		if base == None:
			raise FileNotFoundError("The file or 'static' folder could not be found.")
		return base


	def conn_handler(function):
		def wrapper(*args, **kwargs):
			self.conn = self.connect_to_db()
			dict_cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			ret_value = function(dict_cur, *args, **kwargs)
			dict_cur.close()
			self.conn.close()
			return ret_value
		return wrapper

