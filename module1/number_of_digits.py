"""Library to calculate number of digits
for different algorithms
"""
from math import factorial

def factorial_length(number):
    """Count the number of digits in a factorial number

    Args:
        number (int): integer value to calculate factorial

    Returns:
        int: number of digits for factorial of input
    """

    fac_answer = factorial(number)
    length = len(str(fac_answer)) # convert to a string
    return length # return number of elements
    # return len(str(factorial(number))) same thing but in one line


def main():
    """Driven Function
    """
    number = 120
    digits = factorial_length(number)
    print(f'You have digits {digits} in factorial({number})')


if __name__ == "__main__":
    main()