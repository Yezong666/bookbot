def get_book_text(f):
    file_contents = None
    with open(f) as book:
        file_contents = book.read()
    return file_contents

def calc_words(book_text):
    book_words = book_text.split()
    words = len(book_words)
    return words

def count_char(book_text):
    char_count = {}
    book_text_lower = book_text.lower()
    for char in book_text_lower:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items['num']

def sort_chars(chars_list):
    details = []
    for key in chars_list:
        details.append(None)
        details[len(details)-1] = {'char': key, 'num': chars_list[key]}
    details.sort(reverse=True, key=sort_on)
    
    return details

