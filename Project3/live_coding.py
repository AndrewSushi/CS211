from typing import List

def binary_search(prefix: str , words: List[str]) -> str:
    if len(words) == 0:
        return "No Word"
    index = len(words) // 2
    guess = words[index]
    if guess.startswith(prefix):
        return guess
    elif guess > prefix:
        return binary_search(prefix, words[0:index])
    else:
        return binary_search(prefix, words[index + 1:])