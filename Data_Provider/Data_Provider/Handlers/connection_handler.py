"""
Handles PSQL database connection via psycopg2.
"""

import psycopg2
import psycopg2.extras
import itertools
import io
import os
from psycopg2 import sql
from Data_Provider.Static.creds import get_file_path
import Data_Provider.Models.exceptions as exc

class Connection_Details(object):
   
	def __init__(self, user, password, db_name, port = "5432", address = None):
		env = os.environ
		self.user_name = env["psql_user"] = user
		self.add = env["psql_host"] = "localhost" if address == None else address
		self.pwd = env["psql_pass"] = password
		self.port = env["psql_port"] = port
		self.db = env["psql_db"] = db_name
		self.conn_string = env["psql_conn_string"] = f"postgresql://{self.user_name}:{self.pwd}@{self.add}/{self.db}"
		self.file_path = env["psql_file_path"] = get_file_path() + "\\blank_pages_db.sql"
	
def conn_creator(func):
	def wrapper(*args):
		try:
			conn = connect_to_db()
			dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
			ret_value = func(dict_cur, *args[1:])
		except (Exception, psycopg2.DatabaseError) as e:
			raise exc.Internal_Error("A database error occurred", e)
		finally:
			close_connections(conn)
		return ret_value
	return wrapper

def check_database_exists(info):
	conn = None
	try:
		conn = psycopg2.connect(host=info.add, user=info.user_name, password=info.pwd, port=info.port)
	except (Exception, psycopg2.DatabaseError):
		raise exc.Service_Unavailable("Database Provider could not be reached.")
	if conn is not None:
		conn.autocommit = True
		curs = conn.cursor()
		curs.execute("SELECT datname FROM pg_database")
		databases = curs.fetchall()
		dbs = list(itertools.chain(*databases))
		if info.db in dbs:
			close_connections(conn)
			conn = connect_to_db()
			curs = conn.cursor()
			try:
				curs.execute(sql.SQL("SELECT 'blank_pages.blacklist'::regclass;"))
			except (Exception, psycopg2.DatabaseError):
				read_sql_from_file(conn)
		else:
			create_database(info.db)
	else:
		raise exc.Service_Unavailable("Database Provider could not be reached.")

def connect_to_db():
	try:
		conn = psycopg2.connect(os.environ["psql_conn_string"])
		conn.autocommit = True
	except (Exception, psycopg2.DatabaseError) as e:
		raise exc.Service_Unavailable("Unable to connect to the database server.", e)
	return conn

def create_database(db_name = None):
	name_ = self.db if db_name == None else db_name
	conn = psycopg2.connect(host="localhost", user="postgres", password="postgres", port="5432")
	conn.autocommit = True
	conn.cursor().execute(sql.SQL("CREATE DATABASE {name}").format(name=sql.Identifier(name_)))
	close_connections(conn)
	read_sql_from_file()

def close_connections(conn):
	conn.cursor().close()
	conn.close()

def read_sql_from_file(conn = None):
	if conn is None:
		conn = connect_to_db()
	curs = conn.cursor()
	curs.execute("DROP SCHEMA IF EXISTS blank_pages;")
	curs.execute("CREATE SCHEMA blank_pages;")
	curs.execute(open(os.environ["psql_file_path"], "r").read())
	close_connections(conn)





