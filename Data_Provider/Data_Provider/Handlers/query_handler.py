from .connection_handler import Connection_Handler
from psycopg2 import sql
import psycopg2
import psycopg2.extras

class Query_Handler(Connection_Handler):

	class _Connecter(object):

		def __init__(self, parent_, func):
			self.parent = parent_
			self.func = func

		def __call__(self):
			def wrapper(*args, **kwargs):
				conn = self.parent.connect_to_db()
				dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
				ret_value = self.func(dict_cur, *args, **kwargs)
				dict_cur.close()
				conn.close()
				return ret_value
			return wrapper

	def __init__(self, name, pwd, db):
		self.name = name
		self.pwd = pwd
		self.db = db
		super().__init__(name, pwd, db)

	def create_inner(self):
		return Query_Handler._Connecter(self)

	@_Connecter
	def get_data(cursor, fields_, table_, search_column_, id_):
		cursor.execute(
        sql.SQL("""
			SELECT {fields} from {table}
			WHERE {search_column} = '{id}';
		""").
            format(fields=sql.Identifier(fields_),
				table=sql.Identifier(table_),
				searc_column=sql.Identifier(search_column_),
                   id=sql.Identifier(id_)))
		return curs.fetchone()

	@_Connecter
	def get_all_data(cursor, table_):
		cursor.execute(
        sql.SQL("SELECT * FROM {table};").
            format(table=sql.Identifier(table_)))
		return curs.fetchall()

	@_Connecter
	def update_data(cursor, table_, values_, search_column_, id_):
		cursor.execute(
        sql.SQL("""
			UPDATE {table}
			SET {values}
			WHERE {search_column} = {id};
		""").
            format(table=sql.Identifier(table_),
                   values=sql.Identifier(values_),
				   search_column=sql.Identifier(search_column_),
				   id=sql.Identifier(id_)))
	
	@_Connecter
	def add_data(cursor, table_, columns_, values_):
		cursor.execute(sql.SQL("""
			INSERT INTO {table} ({columns})
			VALUES ({values});
		""").format(table=sql.Identifier(table_),
					columns=sql.Identifier(columns_),
					values=sql.Identifier(values_)))

	@_Connecter
	def delete_data(cursor, table_, search_column_, id_):
		cursor.execute(
        sql.SQL("DELETE FROM {table} WHERE {search_column} = '{id}';").
            format(table=sql.Identifier(table_),
				   search_column=sql.Identifier(search_column_),
                   id=sql.Identifier(id_)))

	@create_inner	
	def wipe_data(cursor, table_):
		cursor.execute(
        sql.SQL("DELETE FROM {table};").
            format(table=sql.Identifier(table_)))

	def check_connection(cls):
		super.check_database_exists()
