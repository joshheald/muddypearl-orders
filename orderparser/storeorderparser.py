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
	identifier = "Email: "
	if order is None:
		return None
	if identifier in order:
		order += "\n"
		index = order.find(identifier) + len(identifier)
		endOfLine = order.find("\n", index)
		return order[index:endOfLine]
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
