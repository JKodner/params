class params(object):
	def __init__(self, *args): 
		new_dict = {}
		for x, y in enumerate(args):
			name = "p%s" % (x+1)
			new_dict.update({name: y})
		self.__dict__ = new_dict
	def call(self, func):
		args = tuple(self.__dict__.values())
		return eval("func" + str(args))