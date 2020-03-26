"""
Handles requests and responses.
"""

from Data_Provider.Handlers import article_handler, author_handler, source_handler
from Data_Provider.Static.creds import psql_creds
from Data_Provider.Models.statuses import get_status
from flask import json, Response

creds = psql_creds()

authors = author_handler.Author_Handler(creds[0], creds[1], creds[2])
articles = article_handler.Article_Handler(creds[0], creds[1], creds[2])
sources = source_handler.Source_Handler(creds[0], creds[1], creds[2])

def create_response(stat_code, obj = None):
	data = json.dumps(obj) if obj != None else "No Data"
	return Response(
			response=data,
			status=stat_code,
			mimetype="application/json"
		)

def create_error_response(stat_code):
	error_data = ("Error_Message" : get_status(stat_code))
	return create_response(stat_code, error_data)

def get_req_handler(table, mass_dat, phrase, search_col ):
	auth = authors.get_all_data if mass_dat else authors.get_data
	arti = articles.get_all_data if mass_dat else articles.get_data
	sour = sources.get_all_data if mass_dat else sources.get_data
	switcher = {
		"au" : auth,
		"ar" : arti,
		"sr" : sour
		}
	func = switcher.get(table, None)
	if func != None:
		if mass_dat:
			return func()
		else:
			return func(search_col, phrase)
	else:
		return AttributeError("Invalid Data Provided")

def post_req_handler(table, vals):
	func = authors.add_data if table == "au" else articles.add_data if table == "ar" else sources.add_data if table == "sr" else None
	if func == None:
		return AttributeError("Invalid Data Provided")
	func(vals)
	return True

def put_req_handler(table, vals, col, phrase,):
	func = authors.update_data if table == "au" else articles.update_data if table == "ar" else sources.update_data if table == "sr" else None
	if func == None:
		return AttributeError("Invalid Data Provided")
	func(vals, col, phrase)
	return True

def del_req_handler(table, mass_dat, phrase):
	auth = authors.wipe_data if mass_dat else authors.delete_data
	arti = articles.wipe_data if mass_dat else articles.delete_data
	sour = sources.wipe_data if mass_dat else sources.delete_data
	switcher = {
		"au" : auth,
		"ar" : arti,
		"sr" : sour
		}
	func = switcher.get(table, None)
	if func != None:
		if mass_dat:
			func()
		else:
			func(phrase)
			return True
	else:
		return AttributeError("Invalid Data Provided")