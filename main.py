from stats import get_book_text
from stats import calc_words
from stats import count_char
from stats import sort_chars
from stats import sort_on
import sys

def main():
    print (sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    

    file_contents = get_book_text(book_path)
    num_words = calc_words(file_contents)
    characters = count_char(file_contents)
    sort_characters = sort_chars(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_characters:
        char = i['char']
        num = i['num']
        if char.isalpha() == 1:
            print (f'{char}: {num}')
    print("============= END ===============")

main()
