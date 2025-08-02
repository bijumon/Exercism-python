
def is_pangram(sentence: str) -> bool:
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    for char in sentence.lower():
        if char in alphabets:
            alphabets.remove(char)
    return True if not alphabets else False