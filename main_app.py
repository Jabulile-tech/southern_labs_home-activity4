# Author: Jabulile Gamede

import random
import datetime
import data_utils

def main():
    """
    The function generates random transactions and displays a full report, starting with today's date, the random numbers and the average transaction.
    """

    # Generating a list of 5 random transaction amounts between 50 ans 500 using the random module
    transaction_amounts = (
        random.randint(50, 500),
        random.randint(50, 500),
        random.randint(50, 500),
        random.randint(50, 500),
        random.randint(50, 500)
    )

    # Retrieving today's date using the datetime module
    current_date = datetime.date.today()

    # Calculating the average amount using the custom module data_utils 
    avg_amount = data_utils.calculate_average(transaction_amounts)

    # Formatting the calculated average into Rands 
    formatted_avg = data_utils.format_currency(avg_amount)

    # Printing the summary of the report 
    print("Date:" + str(current_date))
    print("Generated value:" + str(transaction_amounts))
    print("Average Transaction:" + str(formatted_avg))

if __name__ == "__main__": 
    main()
