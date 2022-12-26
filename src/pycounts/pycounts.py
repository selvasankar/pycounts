from string import punctuation
from collections import Counter

def load_text(input_file):
    """ Load the text file and return the content as text"""
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    "Change text to lower case and remove puncutuations"
    text = text.lower()

    for p in punctuation:
        text.replace(p, "")
    return text

def count_words(input_file):
    """Count the words in the text file and return"""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)


