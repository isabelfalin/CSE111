import math 
from datetime import datetime

print()
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inchees (ex 15): "))

within_parenthesis = (width * aspect_ratio + 2540 * diameter)
no_parenthesis = (math.pi * width ** 2 * aspect_ratio)
volume = (no_parenthesis * within_parenthesis / 10000000000)

print(f"The approximate volume is {volume:.02f} liters. ")

wants_to_buy = input("Do you want to buy tires with the dimensions you entered? ")

if wants_to_buy.lower() == "yes":
    phone_number = input("Phone Number: ")
else:
    phone_number = ''

current_date_and_time = datetime.now()

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.02f}, {phone_number}", file=volumes_file)
