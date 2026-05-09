#!/usr/bin/python3
import sys


def factorial(n):
    """
    Description:
        Calculates the factorial of a number using recursion.

    Parameters:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Description:
    Retrieves the number from the command line,
    calculates its factorial, and prints the result.

Parameters:
    sys.argv[1] (str): Command-line argument representing the number.

Returns:
    None
"""

f = factorial(int(sys.argv[1]))
print(f)
