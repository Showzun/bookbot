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

# support function for sort
def sort_on(item):
    return item["num"]

# moves the dict to a new list of  dicts with the key values [{"char": $value, "num": $int}] and then sorts them
def sort_chars(char_count):
    new_list = list()
    for char in char_count:
        new_list.append({"char": char, "num": char_count[char]})
    new_list.sort(key=sort_on, reverse=True)
    return new_list