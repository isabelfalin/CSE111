def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input("Enter the first odometer reading in (miles): "))
    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input("Enter the second odometer reading in (miles): "))
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon.")
    print(f"{lp100k:.2f} liters per 100 kilometers.")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = ((end_miles - start_miles) / amount_gallons)
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Return: Fuel efficiency in miles per gallon.
    """
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = (235.215 / mpg)
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return lp100k

# Call the main function so that
# this program will start executing.
main()