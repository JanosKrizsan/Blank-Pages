import configparser
import io
import os

def psql_creds():
	creds = read_creds_from_ini()
	if creds == None or creds == []:
		save_creds_to_ini()
		creds = read_creds_from_ini()
	return creds

def get_cred_inputs():
	name = input("Provide the user name :")
	pwd = input("Provide the password :")
	db = input("Provide the database name :")
	return [name, pwd, db]

def save_creds_to_ini():
	details = get_cred_inputs()
	config = configparser.ConfigParser()
	config['creds'] = {'name' : f'{details[0]}',
					'pwd' : f'{details[1]}',
					'db' : f'{details[2]}'}
	path = get_file_path() + "\\settings.ini"
	operation = "x"
	if os.path.exists(path):
		operation = "w"
	with open(path, operation) as conf_file:
		config.write(conf_file)

def read_creds_from_ini():
	config = configparser.ConfigParser()
	config.read(get_file_path() + "\\settings.ini")
	if config.has_section('creds'):
		creds = []
		for v in config['creds'].values():
			creds.append(v)
		return creds
	return None

def get_file_path():
	base = None
	dirs =[dir for dir in os.listdir(os.path.abspath(os.getcwd())) if os.path.isdir(dir)]
	for dir in dirs:
		if "Static" in os.listdir(dir):
			base = os.path.abspath(dir) + "\Static"
			break
	if base == None:
		raise FileNotFoundError("The file or 'static' folder could not be found.")
	return base