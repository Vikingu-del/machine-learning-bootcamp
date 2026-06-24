import string
from typing import List
import sys


def filter_words(sentence: str, nr_words: int) -> List[str]:
    clean_sentence = sentence.translate(
        str.maketrans('', '', string.punctuation)
    )
    words = clean_sentence.split()
    filtered = [word for word in words if len(word) > nr_words]
    return filtered


def main():
    if len(sys.argv) != 3:
        print("Usage: python filterwords.py <sentence> <nr_words>")
        sys.exit(1)

    sentence = sys.argv[1]
    try:
        nr_words = int(sys.argv[2])
    except ValueError:
        print("Error: nr_words must be an integer")
        sys.exit(1)

    filtered_words = filter_words(sentence, nr_words)
    print(filtered_words)


if __name__ == "__main__":
    main()
