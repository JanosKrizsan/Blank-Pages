"""
Created exceptions.
"""

from Data_Provider.Models.statuses import get_status

class Error(Exception):
	
	def __init__(self, *args):
		self.message = args[0] if args else "An Error Just Occurred"

	def __str__(self):
		return f"{self.message}"

class Accepted(Error):

	def __init__(self, *args):
		self.err_code = 202
		return super().__init__(*args)

	def __str__(self):
		return f"Accepted : {super().__str__()}"

class No_Content(Error):

	def __init__(self, *args):
		self.err_code = 204
		return super().__init__(*args)

	def __str__(self):
		return f"No Content : {super().__str__()}"

class Bad_Request(Error):

	def __init__(self, *args):
		self.err_code = 400
		return super().__init__(*args)

	def __str__(self):
		return f"Bad Request : {super().__str__()}"

class Unauthorized(Error):

	def __init__(self, *args):
		self.err_code = 401
		return super().__init__(*args)

	def __str__(self):
		return f"Unauthorized : {super().__str__()}"

class Forbidden(Error):

	def __init__(self, *args):
		self.err_code = 403
		return super().__init__(*args)

	def __str__(self):
		return f"Forbidden : {super().__str__()}"

class Not_Found(Error):

	def __init__(self, *args):
		self.err_code = 404
		return super().__init__(*args)

	def __str__(self):
		return f"Not Found : {super().__str__()}"

class Conflict(Error):

	def __init__(self, *args):
		self.err_code = 409
		return super().__init__(*args)

	def __str__(self):
		return f"Conflict : {super().__str__()}"

class I_Am_A_Hal(Error):

	def __init__(self, *args):
		self.err_code = 418
		return super().__init__(*args)

	def __str__(self):
		return f"I can't let you do that Dave : {super().__str__()}"

class Internal_Error(Error):

	def __init__(self, *args):
		self.err_code = 500
		return super().__init__(*args)

	def __str__(self):
		return f"Internal Error : {super().__str__()}"

class Not_Implemented(Error):

	def __init__(self, *args):
		self.err_code = 501
		return super().__init__(*args)

	def __str__(self):
		return f"Not Implemented : {super().__str__()}"

class Service_Unavailable(Error):

	def __init__(self, *args):
		self.err_code = 503
		return super().__init__(*args)

	def __str__(self):
		return f"Service Unavailable : {super().__str__()}"
