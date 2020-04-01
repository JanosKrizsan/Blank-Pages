class Author_Id_Base(object):

	def __init__(self):
		pass

	@property
	def prop_author_id(self):
		return self.author_id

	@prop_author_id.setter
	def prop_author_id(self, value):
		self.author_id = value
