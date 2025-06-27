def steps(number):
    step = 0
    if number > 0:
        while number > 1:
            step += 1
            if number % 2 == 0:
                number = number / 2
            else:
                number = (number * 3) + 1
    else:
        raise ValueError("Only positive integers are allowed")
    return step
