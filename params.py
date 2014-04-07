class params(object):
	"""Params Class:

	This class is a collection of parameters that can be reused for any function. Any type
	can be inputted."""
	def __init__(self, *args): 
		new_dict = {}
		for x, y in enumerate(args):
			name = "p%s" % (x+1)
			new_dict.update({name: y})
		self.__dict__ = new_dict
	def call(self, func):
		"""Calls a function, with the function's parameters being the object's __dict__ values."""
		args = tuple(self.__dict__.values())
		try:
			return eval("func" + str(args))
		except Exception, e:
			raise ValueError("Given Function is not valid for calling: %s" % e)