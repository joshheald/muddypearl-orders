import datetime
import sys
from muddypearl import mputils


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
	full_name = mputils.text_for_identifier("Name:", "order text")
	return ' '.join(full_name.split()[:-1])

if __name__ == '__main__':
	inFile = sys.argv[1]
	outFile = sys.argv[2]

	with open(inFile,'r') as i:
		lines = i.readlines()

		order_strings = order_strings_from_lines(lines)

		with open(outFile,'w') as o:
			for line in order_strings:
				o.write(line+"\n")
