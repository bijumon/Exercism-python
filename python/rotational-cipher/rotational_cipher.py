
def rotate(text: str, key: int) -> str:
    chars = "abcdefghijklmnopqrstuvwxyz"

    new_chars = chars[key:] + chars[:key]
    trans_table = str.maketrans(chars + chars.upper(), new_chars + new_chars.upper())
    return text.translate(trans_table)
