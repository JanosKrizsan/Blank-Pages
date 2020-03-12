from .model_base import ModelBase

class Author(ModelBase):

	def __init__(self):
		pass

	@property
	def prop_passhash(self):
		return self.passhash

	@property
	def prop_articles_written(self):
		return self.articles_written

	@prop_passhash.setter
	def prop_passhash(self, value):
		self.passhash = value

	@prop_articles_written.setter
	def prop_articles_written(self, value):
		self.articles_written = value
