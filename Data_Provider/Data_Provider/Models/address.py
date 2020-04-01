from .id_base import Id_Base
from .author_id_base import Author_Id_Base

class Address(Id_Base, Author_Id_Base):

	def __init__(self):
		pass

	@property
	def prop_address(self):
		return self.address

	@prop_address.setter
	def prop_address(self, value):
		self.address = value