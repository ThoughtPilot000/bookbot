from stats import count_words, count_characteres, get_book_text, dict_to_list

book_path = "books/frankenstein.txt"

def main():
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {count_words(book_path)} total words")
	print("--------- Character Count -------")
	for i in dict_to_list(count_characteres(get_book_text(book_path))):
		if i["char"].isalpha():
			print(f"{i["char"]}: {i["num"]}")
	print("============= END ===============")

main()