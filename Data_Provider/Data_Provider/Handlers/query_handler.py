from .connection_handler import Connection_Handler as conn
from psycopg2 import sql
import psycopg2
import abc

class Query_Handler(object, metaclass=abc.ABCMeta):

	@classmethod
	def __init__(cls, name = "postgres", pwd = "postgres", db = "blank_pages_db"):
		cls.conn = conn(name, pwd, db)

	@classmethod
	def GetData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def GetAllData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def UpdateData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def UpdateBulkData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def DeleteData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def WipeData(cls):
		curs = cls.conn.cursor()
		cursor.execute(
        sql.SQL("select {col} from {table} ").
            format(col=sql.Identifier(your_column),
                   table=sql.Identifier('your_table')))

	@classmethod
	def close_connections(cls):
		cls.conn.close_connections()

	@classmethod
	def check_connection(cls):
		cls.conn.check_database_exists()