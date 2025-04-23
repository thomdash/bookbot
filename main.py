from stats import number_of_words
from stats import each_character
from stats import get_book_text
from stats import sorted_list
import sys 


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = number_of_words(book_text)
    char_count = each_character(book_text)
    sorted_chars = sorted_list(char_count)
    try: 
        book_text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha(): 
            print(f"{char}: {count}")
    print("============= END ===============")



main()