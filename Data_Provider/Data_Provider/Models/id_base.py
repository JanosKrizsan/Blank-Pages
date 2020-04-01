class Id_Base(object):

	def __init__(self):
		pass

	@property
	def prop_id(self):
		return self.id

	@prop_id.setter
	def prop_id(self, value):
		self.id = value