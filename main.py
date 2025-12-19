from stats import count_words, count_characteres, get_book_text

book_path = "books/frankenstein.txt"

def main():
	print(f"Found {count_words(book_path)} total words \n {count_characteres(get_book_text(book_path))}")

main()