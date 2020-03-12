from .connection_handler import Connection_Handler as conn
from psycopg2 import sql
import psycopg2
import abc

class Query_Handler(object, metaclass=abc.ABCMeta):

	@classmethod
	def __init__(cls, name, pwd, db):
		cls.name = name
		cls.pwd = pwd
		cls.db = db
		cls.open_connection()

	@classmethod
	def GetData(cls, fields_, table_, search_column_, id_):
		curs = cls.conn.cursor()
		curs.execute(
        sql.SQL("""
			SELECT {fields} from {table}
			WHERE {search_column} = '{id}';
		""").
            format(fields=sql.Identifier(fields_),
				table=sql.Identifier(table_),
				searc_column=sql.Identifier(search_column_),
                   id=sql.Identifier(id_)))
		return curs.fetchone()

	@classmethod
	def GetAllData(cls, table_):
		curs = cls.conn.cursor()
		curs.execute(
        sql.SQL("SELECT * FROM {table};").
            format(table=sql.Identifier(table_)))
		return curs.fetchall()

	@classmethod
	def UpdateData(cls, table_, values_, search_column_, id_):
		curs = cls.conn.cursor()
		curs.execute(
        sql.SQL("""
			UPDATE {table}
			SET {values}
			WHERE {search_column} = {id};
		""").
            format(table=sql.Identifier(table_),
                   values=sql.Identifier(values_),
				   search_column=sql.Identifier(search_column_),
				   id=sql.Identifier(id_)))

	@classmethod
	def AddData(cls, table_, columns_, values_):
		curs = cls.conn.cursor()
		curs.execute(sql.SQL("""
			INSERT INTO {table} ({columns})
			VALUES ({values});
		""").format(table=sql.Identifier(table_),
					columns=sql.Identifier(columns_),
					values=sql.Identifier(values_)))

	@classmethod
	def DeleteData(cls, table_, search_column_, id_):
		curs = cls.conn.cursor()
		curs.execute(
        sql.SQL("DELETE FROM {table} WHERE {search_column} = '{id}';").
            format(table=sql.Identifier(table_),
				   search_column=sql.Identifier(search_column_),
                   id=sql.Identifier(id_)))

	@classmethod
	def WipeData(cls, table_):
		curs = cls.conn.cursor()
		curs.execute(
        sql.SQL("DELETE FROM {table};").
            format(table=sql.Identifier(table_)))

	@classmethod
	def open_connection(cls):
		cls.conn = conn(cls.name, cls.pwd, cls.db)

	@classmethod
	def close_connections(cls):
		cls.conn.close_connections()

	@classmethod
	def check_connection(cls):
		cls.conn.check_database_exists()