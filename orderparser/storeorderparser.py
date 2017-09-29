import datetime
import sys

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
	email = text_for_identifier("Email:", order)
	if email is not None:
		email = email.strip()
	return email

def text_for_identifier(identifier, from_text, end_string = "\n"):
	if from_text is None:
		return None
	if identifier in from_text:
		from_text += end_string
		index = from_text.find(identifier) + len(identifier)
		end_index = from_text.find(end_string, index)
		return from_text[index:end_index]
	return None

if __name__ == '__main__':
	inFile = sys.argv[1]
	outFile = sys.argv[2]

	with open(inFile,'r') as i:
		lines = i.readlines()

		order_strings = order_strings_from_lines(lines)

		with open(outFile,'w') as o:
			for line in order_strings:
				o.write(line+"\n")
