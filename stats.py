# split book into words and returns the count
def count_words(string_book):
    list_book = string_book.split()
    return len(list_book)

def count_chars(string_book):
    lower = string_book.lower()
    char_count = dict()
    for char in lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count.update({char: 1})
    return char_count

