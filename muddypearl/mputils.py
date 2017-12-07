def text_for_identifier(identifier, from_text, end_string = "\n"):
	if from_text is None:
		return None
	if identifier in from_text:
		from_text += end_string
		index = from_text.find(identifier) + len(identifier)
		end_index = from_text.find(end_string, index)
		return from_text[index:end_index]
	return None

def order_lines(from_text):
	if from_text is None:
		return None
	order_lines_start = "Item	Price	Quantity	Total\n"
	order_lines_end = "\nSubtotal:"
	if order_lines_start in from_text:
		start_index = from_text.find(order_lines_start) + len(order_lines_start)
		end_index = from_text.find(order_lines_end)
		return from_text[start_index:end_index]