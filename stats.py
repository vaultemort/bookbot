
def get_book_text(path):
    with open(path) as f:

        return f.read()
    
def get_num_words(book):
    words = book.split()
    return len(words)

def get_character_count(book):
    characters = {}
    for character in book:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            characters[character.lower()] += 1
    
    return characters

def get_sorted_analysis(path, word_count, dict):
    sorted_list = []
    for key, value in dict.items():
        sorted_list.append({"char": key, "num": value})

    def sort_on(item):
        return item["num"]  
      
    sorted_list.sort(reverse=True, key=sort_on)
    charcter_list = "\n".join(f"{key['char']}: {key['num']}" for key in sorted_list)
    
    report = f"""============ BOOKBOT ============
Analysing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{charcter_list}
============= END ===============
    """

    return report

    