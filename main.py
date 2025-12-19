def get_book_text(path):
	with open(path) as f:
		contents = f.read()
	return contents