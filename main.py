from stats import count_words, count_chars

# takes a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    string_book = get_book_text("books/frankenstein.txt")
    word_count = count_words(string_book)
    chars_count = count_chars(string_book)
    print(f"{word_count} words found in the document")
    print(chars_count)

main()