"""
Status codes and their relevant response strings.
"""

status_codes = {
	104 : "LOGIN_REQUIRED -> You need to log in to access this data.",
	107 : "BAD_LOGIN -> Login details are incorrect.",
	108 : "USERNAME_TAKEN -> This username is already in... use.",
	200 : "OK -> Successful completion.",
	201 : "CREATED -> Entry successfully created.",
	202 : "ACCEPTED -> The requested action was accepted, but failed to perform.",
	204 : "NO_CONTENT -> This entry could not be found.",
	211 : "CONTENT_UPDATED -> This entry has been successfully updated.",
	219 : "CONTENT_DELETED -> Deletion completed successfully.",
	400 : "BAD_REQUEST -> Malformed request received.",
	401 : "UNAUTHORIZED -> You need to be properly authorized to perform this action.",
	403 : "FORBIDDEN -> You are forbidden to retrieve this entry.",
	404 : "NOT_FOUND -> The space you are trying to reach does not exist.",
	405 : "NOT_ALLOWED -> The method you are trying to use is not allowed on this endpoint.",
	409 : "CONFLICT -> The entry is already present.",
	418 : "I_AM_A_HAL -> I can't let you do that Dave.",
	500 : "INTERNAL_ERROR -> Uh-oh, an unexpected error occurred.",
	501 : "NOT_IMPLEMENTED -> This part has not been fleshed out yet.",
	503 : "SERVICE_UNAVAILABLE -> The service is currently not available."
	}

def get_status(status):
	return status_codes.get(status, None)


