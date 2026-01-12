"""If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. Your program must then 
compute the total amount due by adding sales tax of 6% to the subtotal."""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)

sales_tax = None

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and day_of_week == 1 or 2:
    subtotal = (subtotal * .10 )
    total = (.06 * subtotal)
    sales_tax = (total - subtotal)
    print(f"Sales tax amount: {sales_tax}")
    print(f"Total: {total}")
else:
    total = (sales_tax * subtotal)
    print(f"Sales tax amount: {sales_tax}")
    print(f"Total: {total}")


