class vector2:
	def __init__(self, x_or_vec2, y=None):
		self.x, self.y	= self.__check(x_or_vec2, y)
		#self.value	= [self.x, self.y]

	def __check(self, x_or_vec2, y=None):
		if y == None:
			x = x_or_vec2[0]
			y = x_or_vec2[1]
		else:
			x = x_or_vec2
			y = y
		return int(x), int(y)

	def toString(self, withDot=True):
		if withDot:
			return "".join([str(self.x), ", ", str(self.y)])
		else:
			return "".join([str(self.x), " ", str(self.y)])
	def Value(self):
		return [self.x, self.y]
	def reduce(self, x_or_vec2, y=None):
		x, y = self.__check(x_or_vec2, y)
		self.x = self.x - x
		self.y = self.y - y
	def increase(self, x_or_vec2, y=None):
		x, y = self.__check(x_or_vec2, y)
		self.x = self.x + x
		self.y = self.y + y
	def dive(self, x_or_vec2, y=None):
		x, y = self.__check(x_or_vec2, y)
		print x, y
		self.x = self.x / x
		self.y = self.y / y
	def multiply(self, x_or_vec2, y=None):
		x, y = self.__check(x_or_vec2, y)
		self.x = self.x * x
		self.y = self.y * y
