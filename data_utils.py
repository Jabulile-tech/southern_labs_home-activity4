# Author: Jabulile Gamede


"""
data_utils.py

This utility module gives us a function for data processing such as calculating average and changing the currency
"""

def calculate_average(numbers_list):
    """
    The function calculates the average of a list
    Parameters: numbers_list which is a list of numbers 
    Return: the float of the average of the list and if the list is empty, then 0
    """
    total = sum(numbers_list)
    count = 5

    return total / count


def format_currency(amount):
    """
    The function gives us the amount calculated in rands(R)
    Parameters: amount calculated as a float or integer 
    Returns: the string of the amount calculated in rands(R)
    """
    return "R" + str(amount)


