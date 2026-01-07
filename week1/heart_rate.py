"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#Ask for persons age 
print()
age = int(input("How old are you? "))

#Computs slowest and fastest rates
max_rate = 220 - age
min_range = .65 * max_rate
max_range = .85 *max_rate

#Outputs slowest and fastest rates
print(f"Your ideal heartrate range is between {min_range:.0f} BPM and {max_range:.0f} BPM ")


