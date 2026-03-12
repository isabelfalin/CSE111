import csv
from datetime import datetime, timedelta
#request dicionary
PRODUCT_NUMBER_INDEX = 0
QUANTITY_INDEX = 1

#products dictionary
PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

def main():
    try:
        products_dict = read_dictionary("products.csv", PRODUCT_INDEX)

        # Print the product compound dictionary.
        print("Guppies Store")
        print() 
        print("Requested Items:")
        process_request("request.csv", products_dict)
    
    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print("Error: missing file")

    except KeyError as key_err:
        print()
        print("Error: unknown product ID in the request.csv file")
        print(type(key_err).__name__, key_err, sep=": ")
        

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

def process_request(filename, products_dict):
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        total_items = 0
        total_price = 0


        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])
                product = products_dict[product_number]

                name = product[NAME_INDEX]
                price = product[PRICE_INDEX]

                total_items = total_items + quantity
                total_price = total_price + float(price) * quantity
        
                print(f"{name}: {quantity} @ {price}")

        sales_tax = .06 * total_price
        big_boy_number = sales_tax + total_price

        current_date_and_time = datetime.now()

        return_date = current_date_and_time + timedelta(days=7)
    
        print()
        print(f"Number of items: {total_items}")
        print(f"Subtotal: {total_price:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {big_boy_number:.2f}")
        print()
        print("Thanks for shopping with the Guppies!!")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
        print()
        print(f"This item can be returned until: {return_date: %a %b %d %H:%M:%S %Y}")



# Call main to start this program.
if __name__ == "__main__":
    main()