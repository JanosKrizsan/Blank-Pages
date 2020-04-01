from .id_base import Id_Base

class ModelBase(Id_Base):

	def __init__(self):
		pass

	@property
	def prop_name(self):
		return self.name

	@prop_name.setter
	def prop_name(self, value):
		self.name = value