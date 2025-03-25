import sys
from stats import count_words
from stats import count_characters
from stats import sorted_list



def get_book_text(filepath):
    with open(filepath) as content:
        book_string = content.read()
    return book_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        booktext = get_book_text(filepath)
        words = count_words(booktext)
        character_dict = count_characters(booktext)
        dict_list_sorted = sorted_list(character_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for item in dict_list_sorted:
            print(f"{item["character"]}: {item["count"]}")
        print("============= END ===============")


main()