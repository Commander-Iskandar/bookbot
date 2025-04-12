# This function counts the number of words in a given text string
def count_words(text):
    # Use .split() to break the text into a list of words, splitting on whitespace
    words = text.split()
    # Return the total number of words found
    return len(words)

# This function creates a dictionary counting how often each character appears in the text
def get_char_count(text):
    # Initialize an empty dictionary to store character counts
    character_count_dict = {}

    # Convert the text to lowercase so 'A' and 'a' are counted as the same character
    lower_text = text.lower()

    # Loop through each character in the lowercase text
    for char in lower_text:
        # If the character is already in the dictionary, increase its count
        if char in character_count_dict:
            character_count_dict[char] += 1
        # If it's not in the dictionary yet, add it with an initial count of 1
        else:
            character_count_dict[char] = 1

    # Return the complete dictionary of characters and their counts
    return character_count_dict

# This helper function is used during sorting to extract the count value from each dictionary
# It's passed as the "key" function in the .sort() method
def sort_on(dict_item):
    return dict_item["count"]

# This function takes a dictionary of character counts and turns it into a sorted list
# Each item in the list is a dictionary with "character" and "count" keys
def sort_char(character_dict):
    # Create an empty list to hold each character/count dictionary
    sorted_list = []

    # Loop through each character and its count in the original dictionary
    for char in character_dict:
        # Create a small dictionary for this character and its count
        dict_pair = {
            "character": char,
            "count": character_dict[char]
        }

        # Add it to the sorted list
        sorted_list.append(dict_pair)

    # Sort the list of dictionaries by count in descending order
    sorted_list.sort(reverse=True, key=sort_on)

    # Return the sorted list of character/count dictionaries
    return sorted_list
