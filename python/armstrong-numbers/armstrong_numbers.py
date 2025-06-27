def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]

    length = len(digits)
    total = 0
    for num in digits:
        total += (num ** length)
    return number == total
