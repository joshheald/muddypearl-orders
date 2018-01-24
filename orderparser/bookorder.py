class BookOrder(object):
	"""docstring for BookOrder"""
	def __init__(self, order, book, quantity, price):
		super(BookOrder, self).__init__()
		self.order = order
		self.book = book
		self.quantity = quantity
		self.price = price.strip('£')
		