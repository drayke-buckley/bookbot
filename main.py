from typing import Dict

def main(path: str):
    with open(path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {path} ---")
    print(f"{num_words(file_contents)} words found in the document")
    print("")
    chars_and_counts = count_chars(file_contents)
    for character, counter in chars_and_counts.items():
        print(f"The '{character}' character was found {counter} times")
    print("--- End report ---")

def num_words(string: str) -> int:
    return(len(string.split()))

def count_chars(string: str) -> Dict:
    chars_and_count = {}
    for char in string:
        if char not in ("abcdefghijklmnopqrstuvwxyz"):
            continue
        char = char.lower()
        if char in chars_and_count:
            chars_and_count[char] += 1
        else:
            chars_and_count[char] = 1
    chars_and_count = {k: v for k, v in sorted(chars_and_count.items(), key=lambda item: item[1], reverse=True)}
    return chars_and_count

main("books/frankenstein.txt")