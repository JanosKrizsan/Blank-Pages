class ModelBase(object):

	@property
	def prop_id(self):
		return self.id

	@property
	def prop_name(self):
		return self.name

	@prop_id.setter
	def prop_id(self, value):
		self.id = value

	@prop_name.setter
	def prop_name(self, value):
		self.name = value