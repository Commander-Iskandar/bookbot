# Import the built-in sys module to handle command-line arguments
import sys

# Import the functions you'll use from stats.py
from stats import (
    count_words,       # Returns the total number of words in the input text
    get_char_count,    # Returns a dictionary of character frequencies (lowercase)
    sort_char          # Converts the character dictionary into a sorted list of dictionaries
)

# The main function is the entry point of the program
def main():
    # If the user didn't provide a file path, print usage instructions and exit
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with a non-zero status code to indicate failure

    # Use the second command-line argument as the path to the book file
    book_path = sys.argv[1]

    # Read the full text of the book from the specified file path
    text = get_book_text(book_path)

    # Count how many words are in the text
    num_words = count_words(text)

    # Create a dictionary where each key is a character and the value is how often it appears
    char_dict = get_char_count(text)

    # Convert the dictionary to a sorted list of dictionaries,
    # sorted from most to least frequent by character count
    sorted_char_list = sort_char(char_dict)

    # Print a formatted summary of the analysis
    print_report(book_path, num_words, sorted_char_list)

# This function opens a file and returns its entire contents as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# This function prints the final report, including word and character counts
def print_report(book_path, num_words, sorted_char_list):
    # Print the header with the book path
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Print the total number of words found
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Print the character count header
    print("--------- Character Count -------")

    # Loop through the sorted list of character data
    for item in sorted_char_list:
        # Only print alphabetic characters (ignore symbols, whitespace, etc.)
        if item["character"].isalpha():
            # Print in the format: e: 44538
            print(f"{item['character']}: {item['count']}")

    # Print the footer
    print("============= END ===============")

# Call main() when the script is run
main()
