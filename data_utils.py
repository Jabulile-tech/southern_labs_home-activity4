# Author: Jabulile Gamede


"""
data_utils.py

This utility module gives us a helper function for data processing like calculating average and changing the currency
"""

def calculate_average(numbers_list):
    """
    The function calculates the average of a lis
    Parameters: numners_list (list): A list of numbers 
    Return: float: the average of the list and 0 if list is empty
    """
    if not numbers_list:
        return 0.0 
    return sum(numbers_list) / len(numbers_list)

def format_currency(amount):
    """
    The function formats the number as rands
    Parameters: amount as a float or int 
    Returns: str of the amount as rands
    """
    return f"R{amount:.2f}"


