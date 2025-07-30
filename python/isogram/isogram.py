
def is_isogram(text: str) -> bool:
    chars = ''.join(filter(str.isalnum, text)).lower()
    return len(chars) == len(set(chars))
