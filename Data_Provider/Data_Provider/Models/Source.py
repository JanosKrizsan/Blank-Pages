from .model_base import ModelBase

class Source(ModelBase):

	def __init__(self):
		pass

	@property
	def prop_source_data(self):
		return self.source_data

	@property
	def prop_parent_article_id(self):
		return self.parent_artice_id

	@prop_source_data.setter
	def prop_source_data(self, value):
		self.source_data = value

	@prop_parent_article_id.setter
	def prop_parent_article_id(self ,value):
		self.parent_article_id = value