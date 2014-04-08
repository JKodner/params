class params(object):
	"""Params Class:

	This class is a collection of parameters that can be reused for any function. Any type
	can be inputted.

	The parameters are the self.__dict__'s, values, and the keys are represented a strings
	formatted as 'p#' with '#' being the position the value is being inputted."""
	def __init__(self, *args):
		"""obj.__init__(...) initializes obj; see help(type(obj)) for signature"""
		from collections import OrderedDict
		new_dict = {}
		for x, y in enumerate(args):
			name = "p%s" % (x+1)
			new_dict.update({name: y})
		new_dict = OrderedDict(sorted(new_dict.items()))
		self.__dict__ = new_dict
	def __repr__(self):
		"""obj.__repr__() <==> repr(obj)"""
		return str(tuple(self.__dict__.values()))
	def __getitem__(self, x):
		"""obj.__getitem__(x) <==> obj[x]"""
		return self.__dict__[x]
	def __setitem__(self, x, y):
		"""obj.__setitem__(x, y) <==> obj[x]=y"""
		from re import match
		max_key = int(max(self.__dict__.keys())[1:]) + 1
		patt = r'p\d+'
		mat = match(patt, x)
		if mat:
			x = mat.group()
		else:
			raise ValueError("Not Valid Key Name")
		if int(x[1:]) != max_key:
			x = "p%s" % str(max_key)
		self.__dict__[x] = y
	def __eq__(self, x):
		self_val = tuple(self.__dict__.values())
		if isinstance(x, params):
			x = tuple(x.__dict__.values())
		return self_val == x
	def __len__(self):
		return len(self.__dict__.values())
	def call(self, func):
		"""Calls a function, with the function's parameters being the object's __dict__ values."""
		args = tuple(self.__dict__.values())
		try:
			return eval("func" + str(args))
		except Exception, e:
			raise ValueError("Given Function is not valid for calling: %s" % e)
	def remove(self, value):
		"""Removes 'value' from the object's __dict__ values."""
		dic = self.__dict__
		for i in dic.keys():
			if dic[i] == value:
				del dic[i]