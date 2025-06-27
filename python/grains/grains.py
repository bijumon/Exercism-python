def square(number):
    if number > 0 and number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_grains = 0
    for grains in range(1,65):
        total_grains += square(grains)
    return total_grains