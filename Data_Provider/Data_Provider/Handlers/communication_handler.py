"""
Handles requests and responses.
"""

from Data_Provider.Handlers import article_handler, author_handler, source_handler
from Data_Provider.Static.creds import psql_creds
from Data_Provider.Models.statuses import get_status
import Data_Provider.Models.exceptions as exc
from flask import json, Response

creds = psql_creds()
data_error = "Invalid data provided."

authors = author_handler.Author_Handler(creds[0], creds[1], creds[2])
articles = article_handler.Article_Handler(creds[0], creds[1], creds[2])
sources = source_handler.Source_Handler(creds[0], creds[1], creds[2])

def create_response(stat_code, obj = None):
	data = json.dumps(obj) if obj != None else f"No Response Data: {get_status(stat_code)}"
	return Response(
			response=data,
			status=stat_code,
			mimetype="application/json"
		)

def create_error_response(stat_code):
	error_data = {"Error_Message" : get_status(stat_code)}
	return create_response(stat_code, error_data)

def get_req_handler(table, phrase, search_col, mass_dat):
	tbl = table[0:2]
	auth = authors.get_all_data if mass_dat else authors.get_data
	arti = articles.get_all_data if mass_dat else articles.get_data
	sour = sources.get_all_data if mass_dat else sources.get_data
	switcher = {
		"au" : auth,
		"ar" : arti,
		"so" : sour
		}
	func = switcher.get(tbl, None)
	if func != None:
		if mass_dat:
			dat = func()
		else:
			dat = func(search_col, phrase)
		return dat;
	else:
		raise exc.Accepted(data_error, table)

def get_check(method, table, search, data):
    rules = [
        method != "GET",
        not str.isalpha(search),
        data == "0",
        not str.isdigit(data),
        table == None,
        not str.isalpha(table)
        ]
    return any(rules)

def post_req_handler(table, vals):
	func = authors.add_data if "au" in table else articles.add_data if "ar" in table else sources.add_data if "so" in table else None
	if func == None:
		raise exc.Accepted(data_error, table)
	func(vals)
	return True

def put_req_handler(table, vals, col, phrase,):
	func = authors.update_data if "au" in table else articles.update_data if "ar" in table else sources.update_data if "so" in table else None
	if func == None:
		raise exc.Accepted(data_error, table)
	func(vals, col, phrase)
	return True

def del_req_handler(table, phrase, mass_dat):
	tbl = table[0:2]
	auth = authors.wipe_data if mass_dat else authors.delete_data
	arti = articles.wipe_data if mass_dat else articles.delete_data
	sour = sources.wipe_data if mass_dat else sources.delete_data
	switcher = {
		"au" : auth,
		"ar" : arti,
		"so" : sour
		}
	func = switcher.get(tbl, None)
	if func != None:
		if mass_dat:
			func()
		else:
			func(phrase)
		return True
	else:
		raise exc.Accepted(data_error, table)

def endpoint_check(request, method):
	return any([req.method != method, not req.is_json])