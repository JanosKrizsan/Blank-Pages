from .model_base import ModelBase

class Author(ModelBase):

	def __init__(self):
		pass

	@property
	def prop_password(self):
		return self.password

	@property
	def prop_articles_written(self):
		return self.articles_written

	@prop_password.setter
	def prop_password(self, value):
		self.password = value

	@prop_articles_written.setter
	def prop_articles_written(self, value):
		self.articles_written = value
