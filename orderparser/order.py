class Order(object):
	"""docstring for Order"""
	def __init__(self, delivery_handling, placed, transaction_id, billing_address, delivery_address, customer):
		super(Order, self).__init__()
		self.delivery_handling = delivery_handling
		self.placed = placed
		self.transaction_id = transaction_id
		self.billing_address = billing_address
		self.delivery_address = delivery_address
		self.customer = customer
		self.airtable_id = "{}: {}".format(customer.email, transaction_id)
		self.book_orders = []



class Address(object):
	"""docstring for Address"""
	def __init__(self, line_1, line_2, city, postcode, country):
		super(Address, self).__init__()
		self.line_1 = line_1
		self.line_2 = line_2
		self.city = city
		self.postcode = postcode
		self.country = country
		

		