from stats import count_words, count_chars, sort_chars

# takes a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    string_book = get_book_text("books/frankenstein.txt")
    word_count = count_words(string_book)
    print(f"Found {word_count} total words\n--------- Character Count -------")
    chars_count = count_chars(string_book)
    sorted_chars = sort_chars(chars_count)
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()