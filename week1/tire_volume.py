"""Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15):"""

"""v = 
π w2 aw a + 2,540 d
10,000,000,000
"""

import math 

print()
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inchees (ex 15): "))

within_parenthesis = (width * aspect_ratio + 2540 * diameter)
no_parenthesis = (math.pi * width ** 2 * aspect_ratio)
volume = (no_parenthesis * within_parenthesis / 10000000000)

print(f"The approximate volume is {volume:.02f} liters. ")

from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()


"""Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the 
following five values:
1. current date
2. width of the tire
3. spect ratio of the tire
4. diameter of the wheel
5. volume of the tire"""