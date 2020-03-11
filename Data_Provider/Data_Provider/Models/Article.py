from .model_base import ModelBase

class Article(ModelBase):

	def __init__(self):
		pass
	
	@property
	def prop_subtitle(self):
		return self.subtitle

	@property
	def prop_content(self):
		return self.content

	@property
	def prop_fullfilepath(self):
		return self.fullfilepath

	@property
	def prop_author(self):
		return self.author

	@property
	def prop_creationdate(self):
		return self.creationdate

	@property
	def prop_sources(self):
		return self.sources

	@subtitle.setter
	def prop_subtitle(self, value):
		subtitle = value

	@content.setter
	def prop_content(self, value):
		content = value

	@fullfilepath.setter
	def prop_fullfilepath(self, value):
		self.fullfilepath = value

	@author.setter
	def prop_author(self, value):
		self.author = value

	@creationdate.setter
	def prop_creationdate(self, value):
		self.creationdate = value

	@sources.setter
	def prop_sources(self, value):
		self.sources = value
