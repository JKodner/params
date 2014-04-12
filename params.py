class params(object):
	"""Params Class:

	This class is a collection of parameters that can be reused for any function. Any type
	can be inputted.

	The parameters inputted are part of self.__dict__'s values. Their keys in the dictionary
	are the positions at which they were they were inputted. For Example:

	obj = params("a", "b", "c")
	{1: "a", 2: "b", 3: "c"} # obj's __dict__

	Note: self.__dict__'s values are in the order of when they were initialized. Their order
	is preserved by using collections.OrderedDict."""
	def __init__(self, *args):
		"""obj.__init__(...) initializes obj; see help(type(obj)) for signature"""
		from collections import OrderedDict
		new_dict = {}
		for x, y in enumerate(args):
			new_dict.update({x: y})
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
		"""obj.__eq__(x) <==> obj==x"""
		self_val = tuple(self.__dict__.values())
		if isinstance(x, params):
			x = tuple(x.__dict__.values())
		return self_val == x
	def __len__(self):
		"""obj.__len__() <==> len(obj)"""
		return len(self.__dict__.values())
	def __call__(self, func):
		"""obj.__call__(func) <==> obj(func) <==> obj.call(func)"""
		return self.call(func)
	def __iter__(self):
		"""obj.__iter__() <==> iter(obj)"""
		for i in self.__dict__.values():
			yield i
	def __contains__(self, item):
		"""obj.__contains__(x) <==> x in obj"""
		return item in self.__dict__.values()
	def __reversed__(self):
		"""obj.__reversed__() -- return a reverse iterator over the obj's values."""
		return reversed(self.__dict__.values())
	def call(self, func):
		"""Calls a function, with the function's params being the object's __dict__ values.

		Note: A shorter approach to doing this is self(func)."""
		args = tuple(self.__dict__.values())
		try:
			return eval("func" + str(args))
		except Exception, e:
			raise ValueError("Given Function is not valid for calling: %s" % e)
	def insert(self, pos, value):
		"""Inserts given 'value' inside self.__dict__, with it's key being the inputted 'pos'
		value. This function is similar to the insert function belonging to lists.

		Note: 'pos' value must be a positive number, and must be less than self.__dict__'s 
		length."""
		items = self.__dict__.values()
		if not isinstance(pos, int) or pos < 0:
			raise ValueError("'pos' value is not positive integer.")
		elif pos >= len(items):
			raise ValueError("'pos' value is not a position in self.__dict__")
		items.insert(pos, value)
		new_dict = {}
		for x, y in enumerate(items):
			new_dict.update({x: y})
		self.__dict__ = new_dict
	def remove(self, key):
		"""Removes the inputted self.__dict__'s key."""
		from collections import OrderedDict
		dic = self.__dict__
		key = "p%s" % key
		if not dic.get(key):
			raise ValueError("Inputted Key is not valid for removal.")
		del dic[key]
		new_dict = {}
		args = dic.values()
		for x, y in enumerate(args):
			name = "p%s" % (x+1)
			new_dict.update({name: y})
		new_dict = OrderedDict(sorted(new_dict.items()))
		self.__dict__ = new_dict