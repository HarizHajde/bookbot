
filepath = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as content:
        book_string = content.read()
    return book_string



def count_words(booktext):
    word_count = 0
    splitted_strings = booktext.split()
    for string in splitted_strings:
        word_count += 1
    print(f"total number of words in text: {word_count}")



def main():
    booktext = get_book_text(filepath)
    print(booktext)
    count_words(booktext)


main()