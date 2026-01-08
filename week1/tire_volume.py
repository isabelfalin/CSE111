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
no_parenthesis = (math.pi * width * width * aspect_ratio)
volume = (no_parenthesis * within_parenthesis / 10000000000)

print(f"The approximate volume is {volume:.02f} liters. ")