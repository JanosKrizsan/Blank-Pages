import abc

class ModelBase(object, metaclass=abc.ABCMeta):

	@property
	@abc.abstractmethod
	def prop_id(self):
		return self.id

	@property
	@abc.abstractmethod
	def prop_name(self):
		return self.name

	@prop_id.setter
	def prop_id(self, value):
		self.__id_setter__(value)

	@prop_name.setter
	def prop_name(self, value):
		self.__name_setter__(value)

	@abc.abstractmethod
	def __id_setter__(self, value):
		self.id = value

	@abc.abstractmethod
	def __name_setter__(self, value):
		self.name = value
