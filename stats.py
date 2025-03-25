

def count_words(booktext):
    splitted_strings = booktext.split()
    word_count = len(splitted_strings)
    return word_count


def count_characters(booktext):
    character_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for character in booktext:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
    return character_dict

def sorted_list(character_dict):
    character_list = []
    for char, count in character_dict.items():
        character_list.append({"character" : char, "count": count})
    
    def sort_on(character_dict):
        return character_dict["count"]

    character_list.sort(reverse=True, key=sort_on)
    
    return character_list

    


