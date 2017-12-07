class Customer(object):
	"""docstring for Customer"""
	def __init__(self, email, first_name, last_name, newsletter_subscription):
		super(Customer, self).__init__()
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.newsletter_subscription = newsletter_subscription
	
