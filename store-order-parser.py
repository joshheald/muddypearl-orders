import datetime
import sys

def order_strings_from_lines(lines):
	order_strings = []
	order = ""
	for line in lines:
		stripped = line.strip()
		if stripped != "------End Order------":
			order += stripped
		else:
			order_strings.append(order)
			order = ""
	return order_strings

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r') as i:
	lines = i.readlines()

	order_strings = order_strings_from_lines(lines)

	with open(outFile,'w') as o:
		for line in order_strings:
			o.write(line+"\n")
