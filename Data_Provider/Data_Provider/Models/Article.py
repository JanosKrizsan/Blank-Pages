from .model_base import ModelBase

class Article(ModelBase):

	def __init__(self):
		pass
	
	@property
	def prop_sub_title(self):
		return self.sub_title

	@property
	def prop_content(self):
		return self.content

	@property
	def prop_full_file_path(self):
		return self.full_file_path

	@property
	def prop_author_id(self):
		return self.author_id

	@property
	def prop_creation_date(self):
		return self.creation_date

	@property
	def prop_sources(self):
		return self.sources

	@prop_sub_title.setter
	def prop_sub_title(self, value):
		self.sub_title = value

	@prop_content.setter
	def prop_content(self, value):
		self.content = value

	@prop_full_file_path.setter
	def prop_full_file_path(self, value):
		self.full_file_path = value

	@prop_author_id.setter
	def prop_author_id(self, value):
		self.author_id = value

	@prop_creation_date.setter
	def prop_creation_date(self, value):
		self.creation_date = value

	@prop_sources.setter
	def prop_sources(self, value):
		self.sources = value
