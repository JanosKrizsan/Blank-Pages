class Author(object):

	def __init__(self):
		pass

	@property
	def prop_id(self):
		return self.id

	@property
	def prop_name(self):
		return self.name

	@property
	def prop_passhash(self):
		return self.passhash

	@property
	def prop_articles_written(self):
		return self.articles_written

	@id.setter
	def prop_id(self, value):
		id = value

	@name.setter
	def prop_name(self, value):
		self.name = value

	@passhash.setter
	def prop_passhash(self, value):
		self.passhash = value

	@articles_written.setter
	def prop_articles_written(self, value):
		self.articles_written = value
