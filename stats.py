#utility/preperation

def get_book_text(path):
	with open(path) as f:
		contents = f.read()
	return contents

def cut_words(path):
    return get_book_text(path).split()

# count words

def count_words(path):
    word_count = 0
    for i in cut_words(path):
        word_count += 1

    return word_count

#charactere counting

def count_characteres(string):
    charactere_count_dict = {}

    for i in string.lower():
        if i in charactere_count_dict:
            charactere_count_dict[i] += 1
        else:
            charactere_count_dict[i] = 1

    return charactere_count_dict