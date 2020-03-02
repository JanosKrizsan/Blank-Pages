class Source(object):

	def __init__(self):
		pass

	@property
	def prop_id(self):
		return self.id

	@property
	def prop_name(self):
		return self.name

	@property
	def prop_source_data(self):
		return self.source_data

	@property
	def prop_parent_article(self):
		return self.parent_artice

	@id.setter
	def prop_id(self, value):
		self.id = value

	@name.setter
	def prop_name(self, value):
		self.name = value

	@source_data.setter
	def prop_source_data(self, value):
		self.source_data = value

	@parent_artice.setter
	def prop_parent_article(self ,value):
		self.parent_article = value