#
# Formatted string literals (also called f-strings for short) let you include
# the value of Python expressions inside a string by prefixing the string
# with f or F and writing expressions as {expression}
#
# https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
#

""" demonstrate f-strings using an example"""

def two_fer(name="you"):
    """
    A bakery that has a holiday offer where you can buy two cookies 
    for the price of one ("two-fer one!").
    
    Determine what you will say as you give away the extra cookie to a friend 
    """

    answer = f"One for {name}, one for me."
    return answer
