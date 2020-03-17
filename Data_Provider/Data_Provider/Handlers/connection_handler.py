import psycopg2
import psycopg2.extras
import itertools
import io
import os
from psycopg2 import sql

class Connection_Details(object):
   
	def __init__(self, user, password, db_name, port = "5432", address = None):
		env = os.environ
		self.user_name = env["psql_user"] = user
		self.add = env["psql_host"] = "localhost" if address == None else address
		self.pwd = env["psql_pass"] = password
		self.port = env["psql_port"] = port
		self.db = env["psql_db"] = db_name
		self.conn_string = env["psql_conn_string"] = f"postgresql://{self.user_name}:{self.pwd}@{self.add}/{self.db}"
		self.file_path = env["psql_file_path"] = self.get_file_path() + "\\blank_pages_db.sql"
	
	@staticmethod
	def get_file_path():
		base = None
		dirs =[dir for dir in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(dir)]
		for dir in dirs:
			if "Static" in os.listdir(dir):
				base = os.path.abspath(dir) + "\Static"
				break
		if base == None:
			raise FileNotFoundError("The file or 'static' folder could not be found.")
		return base

def conn_creator(func):
	def wrapper(*args, **kwargs):
		conn = connect_to_db()
		dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		vars = args[1:]
		ret_value = func(dict_cur, vars, **kwargs)
		dict_cur.close()
		conn.close()
		return ret_value
	return wrapper

def check_database_exists(info):
	conn = None
	try:
		conn = psycopg2.connect(host=info.add, user=info.user_name, password=info.pwd, port=info.port)
	except (Exception, psycopg2.DatabaseError) as error:
		print("Unable to connect to database server.", error)
	if conn is not None:
		conn.autocommit = True¨
		curs = conn.cursor()
		curs.execute("SELECT datname FROM pg_database")
		databases = curs.fetchall()
		dbs = list(itertools.chain(*databases))
		if info.db in dbs:
			#This always returns false in python, but true in PSQL
			#TODO \\ ask about this
			curs.execute(sql.SQL("""
				SELECT EXISTS (
					SELECT FROM pg_catalog.pg_class c
					JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace
					WHERE  n.nspname = '{datbase}'
					AND    c.relname = 'authors'
					);
			""").format(datbase = sql.Identifier(info.db)))
			exists = curs.fetchone()[0]
			#if exists == False:
			#	read_sql_from_file()
		else:
			create_database(info.db)
	else:
		print("PSQL Database Provider could not be reached.")

def connect_to_db():
	try:
		conn = psycopg2.connect(os.environ["psql_conn_string"])
		conn.autocommit = True
	except (Exception, psycopg2.DatabaseError) as error:
		print("Database does not exist, or another error occurred:", error)
	return conn

def create_database(db_name = None):
	name = self.db if db_name == None else db_name
	conn = psycopg2.connect(host="localhost", user="postgres", password="postgres", port="5432")
	conn.autocommit = True
	conn.cursor().execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
	close_connections(conn)

def close_connections(conn):
	conn.cursor().close()
	conn.close()

def read_sql_from_file():
	conn = connect_to_db()
	conn.cursor().execute(open(os.environ["psql_file_path"], 'r').read())
	close_connections(conn)





