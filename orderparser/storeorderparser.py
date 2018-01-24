import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
import datetime
import csv
from muddypearl import mputils
from order import Order, Address
from customer import Customer
from bookorder import BookOrder


def order_strings_from_lines(lines):
	return strings_from_lines(lines, "------End Order------")

def strings_from_lines(lines, delimiter):
	strings = []
	string = ""
	for line in lines:
		if line.strip() != delimiter:
			string += line
		else:
			strings.append(string)
			string = ""
	return strings

def customer_email_from_order(order):
	email = mputils.text_for_identifier("Email:", order)
	if email is not None:
		email = email.strip()
	if email is None or email == "":
		email = "{firstname}.{lastname}@example.com".format(firstname=customer_first_name(order), lastname=customer_last_name(order))
	return email

def customer_first_name(order):
	full_name = mputils.text_for_identifier("Name:", order)
	return ' '.join(full_name.split()[:-1])

def customer_last_name(order):
	full_name = mputils.text_for_identifier("Name:", order)
	return full_name.split()[-1]

def customer_newsletter_subscription(order):
	newsletter_subscription = mputils.text_for_identifier("Newsletter subscription:", order)
	return newsletter_subscription

def address_from_order(order, identifier):
	address_string = mputils.text_for_identifier(identifier, order, end_string="\n\n")
	if address_string is not None:
		address_lines = address_string.splitlines()
		if len(address_lines) == 5:
			return Address(address_lines[1], "", address_lines[2], address_lines[3], address_lines[4])
		elif len(address_lines) == 6:
			return Address(address_lines[1], address_lines[2], address_lines[3], address_lines[4], address_lines[5])
	return Address("","","","","")

def delivery_handling(order):
	delivery_handling = mputils.text_for_identifier("Delivery & Handling:", order)
	if delivery_handling.strip() == 'FREE':
		return "0.00"
	else:
		return delivery_handling.strip(" \t£")

def book_orders_from_lines(order_lines, order):
	book_orders = []
	for line in order_lines.split("\n"):
		line_fields = line.split("\t")
		if len(line_fields) >= 4:
			book_order = BookOrder(order.airtable_id, line_fields[0], line_fields[2], line_fields[1])
			book_orders.append(book_order)
	return book_orders

def filename_with_suffix(filename, suffix):
	filename_components = filename.split(".")
	return "{}-{}.csv".format(filename_components[0], suffix)

if __name__ == '__main__':
	in_file = sys.argv[1]
	out_file = sys.argv[2]

	with open(in_file,'r') as i:
		lines = i.readlines()

		order_strings = order_strings_from_lines(lines)

		orders = []
		for order in order_strings:
			customer = Customer(customer_email_from_order(order), customer_first_name(order), customer_last_name(order), customer_newsletter_subscription(order))
			billing_address = address_from_order(order, "Billing address:\n")
			delivery_address = address_from_order(order, "Delivery address:\n\n")
			order_model = Order(delivery_handling(order), order.splitlines()[1], mputils.text_for_identifier("Transaction ID:", order), billing_address, delivery_address, customer)
			book_orders = book_orders_from_lines(mputils.order_lines(order), order_model)
			order_model.book_orders = book_orders
			orders.append(order_model)

		customer_file = filename_with_suffix(out_file, "customer")
		with open(customer_file, 'w', newline='') as customer_csvfile:
			csvwriter = csv.writer(customer_csvfile, quoting=csv.QUOTE_MINIMAL)
			for order in orders:
				customer = order.customer
				csvwriter.writerow([customer.email, 
					customer.first_name, 
					customer.last_name, 
					customer.newsletter_subscription, 
					order.transaction_id, 
					order.placed])

		order_file = filename_with_suffix(out_file, "order")
		with open(order_file, 'w', newline='') as order_csvfile:
			csvwriter = csv.writer(order_csvfile, quoting=csv.QUOTE_MINIMAL)
			for order in orders:
				csvwriter.writerow([order.delivery_handling, 
					order.placed, 
					order.transaction_id, 
					order.customer.email, 
					order.billing_address.line_1, 
					order.billing_address.line_2, 
					order.billing_address.city, 
					order.billing_address.postcode, 
					order.billing_address.country, 
					order.delivery_address.line_1, 
					order.delivery_address.line_2, 
					order.delivery_address.city, 
					order.delivery_address.postcode, 
					order.delivery_address.country])

		bookorder_file = filename_with_suffix(out_file, "bookorder")
		with open(bookorder_file, 'w', newline='') as bookorder_csvfile:
			csvwriter = csv.writer(bookorder_csvfile, quoting=csv.QUOTE_MINIMAL)
			for order in orders:
				for book_order in order.book_orders:
					csvwriter.writerow([order.airtable_id,
						book_order.book, 
						book_order.quantity,
						book_order.price
						])