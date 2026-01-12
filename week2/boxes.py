import math

items = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

number_of_boxes = (items / per_box)
 
number_of_boxes = math.ceil(number_of_boxes)

print (f"For {items} items, packing {per_box} items in each box, you will need {number_of_boxes} boxes")
