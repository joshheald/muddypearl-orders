import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
import datetime
import csv
from muddypearl import mputils
from order import Order, Address
from customer import Customer


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
	address_string = mputils.text_for_identifier(identifier, order)
	if address_string is not None:
		address_lines = address_string.splitlines()
		if len(address_lines) == 5:
			return Address(address_lines[0], address_lines[1], address_lines[2], address_lines[3], address_lines[4])
	return None

def delivery_handling(order):
	delivery_handling = mputils.text_for_identifier("Delivery & Handling:", order)
	if delivery_handling == 'FREE':
		return "0.00"
	else:
		return delivery_handling.strip('£')

if __name__ == '__main__':
	inFile = sys.argv[1]
	outFile = sys.argv[2]

	with open(inFile,'r') as i:
		lines = i.readlines()

		order_strings = order_strings_from_lines(lines)

		with open(outFile, 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
			for order in order_strings:
				billing_address = address_from_order(order, "Billing address:")
				shipping_address = address_from_order(order, "Delivery address:")
				order_model = Order(delivery_handling(order), order.splitlines()[1], mputils.text_for_identifier("Transaction ID:", order), billing_address, shipping_address)
				customer = Customer(customer_email_from_order(order), customer_first_name(order), customer_last_name(order), customer_newsletter_subscription(order), order_model)
				csvwriter.writerow([customer.email, customer.first_name, customer.last_name, customer.newsletter_subscription, order_model.transaction_id, order_model.placed])
