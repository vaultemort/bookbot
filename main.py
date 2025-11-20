import sys
from stats import get_num_words, get_book_text, get_character_count, get_sorted_analysis

def main():
    
    try: 
        path = sys.argv[1]
        book = get_book_text(path)
        number_of_words = get_num_words(book)
        character_count = get_character_count(book)
        report = get_sorted_analysis(path, number_of_words, character_count)
        print(report)
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    

if __name__ == "__main__":
    main()