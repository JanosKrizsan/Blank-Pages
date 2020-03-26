"""
Handles, or provides generic queries which are called by sub-handlers for the specific tables.
"""
from .connection_handler import Connection_Details as details, connect_to_db, conn_creator, check_database_exists
from psycopg2 import sql
import psycopg2
import psycopg2.extras

class Query_Handler(object):

	def __init__(self, name, pwd, db):
		self.details = details(name, pwd, db)

	@conn_creator
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
		return cursor.fetchone()

	@conn_creator
	def get_all_data(cursor, vals):
		table_ = vals[0]
		cursor.execute(
        sql.SQL("SELECT * FROM {table};").
            format(table=sql.Identifier(table_)))
		return cursor.fetchall()

	@conn_creator
	def update_data(cursor, table_, values_, search_column_, id_):
		cursor.execute(
        sql.SQL("""
			UPDATE {table}
			SET {values}
			WHERE {search_column} = '{id}';
		""").
            format(table=sql.Identifier(table_),
                   values=sql.Identifier(values_),
				   search_column=sql.Identifier(search_column_),
				   id=sql.Identifier(id_)))

	@conn_creator
	def add_data(cursor, table_, columns_, values_):
		cursor.execute(sql.SQL("""
			INSERT INTO {table} ({columns})
			VALUES ({values});
		""").format(table=sql.Identifier(table_),
					columns=sql.Identifier(columns_),
					values=sql.Identifier(values_)))

	@conn_creator
	def delete_data(cursor, table_, search_column_, id_):
		cursor.execute(
        sql.SQL("DELETE FROM {table} WHERE {search_column} = '{id}';").
            format(table=sql.Identifier(table_),
				   search_column=sql.Identifier(search_column_),
                   id=sql.Identifier(id_)))

	@conn_creator
	def wipe_data(cursor, table_):
		cursor.execute(
        sql.SQL("DELETE FROM {table};").
            format(table=sql.Identifier(table_)))

	def check_connection(self):
		check_database_exists(self.details)

