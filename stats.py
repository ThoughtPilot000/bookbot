def get_book_text(path):
	with open(path) as f:
		contents = f.read()
	return contents

def cut_words(path):
    return get_book_text(path).split()

def count_words(path):
    word_count = 0
    for i in cut_words(path):
        word_count += 1
    
    return word_count