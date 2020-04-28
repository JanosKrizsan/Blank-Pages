"""
Handles, or provides generic queries which are called by sub-handlers for the specific tables.
"""

from .connection_handler import Connection_Details as details, connect_to_db, conn_creator, check_database_exists
import Data_Provider.Models.exceptions as exc
from psycopg2 import sql, extras, errors
import psycopg2

class Query_Handler(object):

	def __init__(self, name, pwd, db):
		self.details = details(name, pwd, db)

	@conn_creator
	def get_data(cursor, fields_, table_, search_column_, search_phrase):
		cursor.execute(
		sql.SQL("""
			SELECT {} from blank_pages.{}
			WHERE {}={};
		""").
			format(sql.SQL(",").join(map(sql.Identifier, fields_)),
				sql.Identifier(table_),
				sql.Identifier(search_column_),
				sql.Literal(search_phrase)))
		entry = cursor.fetchone()
		if entry is None:
			raise exc.No_Content("The entry sought out does not exist.")
		return entry

	@conn_creator
	def get_all_data(cursor, vals):
		table_ = vals[0]
		cursor.execute(
		sql.SQL("SELECT * FROM blank_pages.{table};").
			format(table=sql.Identifier(table_)))
		entries = cursor.fetchall()
		if entries == []:
			raise exc.No_Content("The entries sought out do not exist.")
		return entries

	@conn_creator
	def update_data(cursor, table_, values_, search_column_, phrase_):
		cursor.execute(
		sql.SQL("""
			UPDATE blank_pages.{table}
			SET {values}
			WHERE {search_column} = '{phrase}';
		""").
			format(table=sql.Identifier(table_),
				   values=sql.Identifier(values_),
				   search_column=sql.Identifier(search_column_),
				   phrase=sql.Identifier(phrase_)))

	@conn_creator
	def add_data(cursor, table_, columns_, values_):
		cursor.execute(sql.SQL("""
			INSERT INTO blank_pages.{} ({})
			VALUES ({});
		""").format(sql.Identifier(table_),
					sql.SQL(",").join(map(sql.Identifier, columns_)),
					sql.SQL(",").join(map(sql.Literal, values_))))

	@conn_creator
	def delete_data(cursor, table_, search_column_, phrase_):
		cursor.execute(
		sql.SQL("DELETE FROM blank_pages.{table} WHERE {search_column} = '{phrase}';").
			format(table=sql.Identifier(table_),
					search_column=sql.Identifier(search_column_),
					phrase=sql.Literal(phrase_)))

	@conn_creator
	def wipe_data(cursor, table_):
		cursor.execute(
		sql.SQL("DELETE FROM blank_pages.{table};").
			format(table=sql.Identifier(table_)))

	def check_connection(self):
		check_database_exists(self.details)

