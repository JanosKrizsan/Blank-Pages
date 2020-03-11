import psycopg2
import psycopg2.extras
import itertools
import io
import os
from psycopg2 import sql

class Connection_Handler(object):

	@classmethod
	def __init__(cls, user, password, db_name, port = "5432", address = None):
		cls.user_name = user
		cls.host_add = "localhost" if address == None else address
		cls.password = password
		cls.port = port
		cls.db = db_name
		cls.conn_string = f"postgresql://{cls.user_name}:{cls.password}@{cls.host_add}/{cls.db}"
		cls.file_path = cls.get_relative_path() + "\\blank_pages_db.sql"

	@classmethod
	def check_database_exists(cls):
		cls.conn = None
		try:
			cls.conn = psycopg2.connect(host=cls.host_add, user=cls.user_name, password=cls.password, port=cls.port)
		except (Exception, psycopg2.DatabaseError) as error:
			print("Unable to connect to database server.", error)
		if cls.conn is not None:
			cls.conn.autocommit = True
			curs = cls.conn.cursor()
			curs.execute("SELECT datname FROM pg_database")
			databases = curs.fetchall()
			dbs = list(itertools.chain(*databases))
			if cls.db in dbs:
				#This always returns false in python, but true in PSQL
				#TODO \\ ask about this
				curs.execute(sql.SQL("""
					SELECT EXISTS (
						SELECT FROM pg_catalog.pg_class c
						JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace
						WHERE  n.nspname = '{datbase}'
						AND    c.relname = 'authors'
						);
				""").format(datbase = sql.Identifier(cls.db)))
				exists = curs.fetchone()[0]
				#if exists == False:
				#	self.read_sql_from_file()
			else:
				cls.create_database(cls.db)
		else:
			print("PSQL Database Provider could not be reached.")

	@classmethod
	def connect_to_db(cls):
		try:
			con = psycopg2.connect(cls.conn_string)
			con.autocommit = True
		except (Exception, psycopg2.DatabaseError) as error:
			print("Database does not exist, or another error occurred:", error)
		return con

	@classmethod
	def create_database(cls, db_name = None):
		name = cls.db if db_name == None else db_name
		cls.conn = psycopg2.connect(host="localhost", user="postgres", password="postgres", port="5432")
		cls.conn.autocommit = True
		cls.conn.cursor().execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
		cls.close_connections()

	@classmethod
	def close_connections(cls):
		cls.conn.cursor().close()
		cls.conn.close()

	@classmethod
	def read_sql_from_file(cls):
		conn = cls.connect_to_db()
		conn.cursor().execute(open(cls.file_path, 'r').read())
		cls.close_connections()

	@staticmethod
	def get_relative_path():
		base = None
		dirs =[dir for dir in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(dir)]
		for d in dirs:
			if "Static" in os.listdir(d):
				base = os.path.abspath(d) + "\Static"
				break
		if base == None:
			raise FileNotFoundError("The file or 'static' folder could not be found.")
		return base

	@staticmethod
	def conn_handler(function):
		def wrapper(*args, **kwargs):
			self.conn = self.connect_to_db()
			dict_cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			ret_value = function(dict_cur, *args, **kwargs)
			dict_cur.close()
			self.conn.close()
			return ret_value
		return wrapper

