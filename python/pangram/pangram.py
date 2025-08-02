
def is_pangram(sentence: str) -> bool:
    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    for char in alphabets:
        if char not in sentence.lower():
            return False
    return True