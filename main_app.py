# Author: Jabulile Gamede

import random
import datetime
import data_utils

def main():
    """
    This generates random transactions and displays a report.
    """

    # Generating a list of 5 random transaction amounts between 50 ans 500
    transaction_amounts = [random.randint(50,500) for _ in range(5)]

    # Retrieving today's date
    current_date = datetime.date.today()

    # Getting the average value using the custom module 
    avg_amount = data_utils.calculate_average(transaction_amounts)

    # Formatting the average into Rands 
    formatted_avg = data_utils.format_currency(avg_amount)

    # Printing the summary
    print(f"Date: {current_date}")
    print(f"Generated value: {transaction_amounts}")
    print(f"Average Transaction:{formatted_avg}")

if __name__ == "__main__": 
    main()
