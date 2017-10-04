def text_for_identifier(identifier, from_text, end_string = "\n"):
	if from_text is None:
		return None
	if identifier in from_text:
		from_text += end_string
		index = from_text.find(identifier) + len(identifier)
		end_index = from_text.find(end_string, index)
		return from_text[index:end_index]
	return None