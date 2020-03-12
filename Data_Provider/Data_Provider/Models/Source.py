from .model_base import ModelBase

class Source(ModelBase):

	def __init__(self):
		pass

	@property
	def prop_source_data(self):
		return self.source_data

	@property
	def prop_parent_article(self):
		return self.parent_artice

	@prop_source_data.setter
	def prop_source_data(self, value):
		self.source_data = value

	@prop_parent_article.setter
	def prop_parent_article(self ,value):
		self.parent_article = value