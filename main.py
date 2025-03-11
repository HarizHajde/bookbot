


def get_book_text(filepath):
    with open(filepath) as content:
        return content.read()



def main():
    filepath = "books/frankenstein.txt"
    booktext = get_book_text(filepath)
    print(booktext)

main()