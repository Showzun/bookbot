# takes a filepath and returns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
# split book into words
def split_book(string_book):
    list_book = string_book.split()
    return list_book

def main():
    string_book = get_book_text("books/frankenstein.txt")
    list_book = split_book(string_book)
    print(f"{len(list_book)} words found in the document")

main()