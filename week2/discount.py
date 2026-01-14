"""If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. Your program must then 
compute the total amount due by adding sales tax of 6% to the subtotal."""

#importing the function to let me get the date and time from computer
from datetime import datetime

#getting the current date and time from the computer
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()


sales_tax = None

"""Near the beginning of your program replace the code that asks the user for the 
subtotal with a loop that repeatedly asks the user for a price and a quantity and 
computes the subtotal. This loop should repeat until the user enters "0" for the price."""

#creates a loop that keeps asking for the price of items and the quantity
#Then computes the subtotal

subtotal = 0
quantity = -1
price = -1

while price != 0:
    price = float(input("Please enter the price of item: "))
    if price == 0:
        break
    quantity = int(input("Please enter the quantity of item: "))
    subtotal = (subtotal + (price * quantity))

print()
print(f"The subtotal of all your items is: ${subtotal:.02f}")
print()

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = (.1 * subtotal)
    subtotal = (subtotal - discount )
    sales_tax = (.06 * subtotal)
    total = (sales_tax + subtotal)

    print(f"Discount amount: ${discount:.02f}")
    print(f"Sales tax amount: ${sales_tax:.02f}")
    print(f"Total: ${total:.02f}")
    
else:
    sales_tax = (.06 * subtotal)
    total = (sales_tax * subtotal)
    print(f"Sales tax amount: ${sales_tax:.02f}")
    print(f"Total: ${total:.02f}")


