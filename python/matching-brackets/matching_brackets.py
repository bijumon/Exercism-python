def is_paired(text: str) -> bool:
    pairs = { '}':'{', ']':'[', ')':'(' }
    brackets = []
    for chr in text:
        if chr in '{[(':
            brackets.append(chr)
        elif chr in '}])':
            if not brackets or brackets.pop() != pairs[chr]:
                return False
    return not brackets