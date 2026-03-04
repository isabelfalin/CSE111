import csv
#request dicionary
PRODUCT_NUMBER_INDEX = 0
QUANTITY_INDEX = 1

#products dictionary
PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

def main():
    products_dict = read_dictionary("products.csv", PRODUCT_INDEX)

    # Print the product compound dictionary.
    print("All Products: ")
    print(products_dict)
    print() 
    print("Requested Items:")
    process_request("request.csv", products_dict)

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

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                quantity = row_list[QUANTITY_INDEX]
                product = products_dict[product_number]

                name = product[NAME_INDEX]
                price = product[PRICE_INDEX]

                
                print(f"{name}: {quantity} @ {price}")

# Call main to start this program.
if __name__ == "__main__":
    main()