
filepath = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as content:
        book_string = content.read()
    return book_string



def count_words(booktext):
    splitted_strings = booktext.split()
    word_count = len(splitted_strings)
    print(f"{word_count} words found in the document")



def main():
    booktext = get_book_text(filepath)
    print(booktext)
    count_words(booktext)


main()