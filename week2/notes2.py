#CSE111 focuses on structure of functions. Make variables full names and clear. 
# Space out when using math (around operators)
#Place imports in the beginning of file
#Header - three """ """ gives the purpose, says what you're doing

#in an if statement, don't want to print something yet use a "pass" statement, or use three dots
#pypi.org has all packages that you can intall on python, all free
#in Math there is an import called, "random" this picks a random number, you can have a range.

#import datetime finds the date of the day and the current time
#import calender prints the year in a calender format

#will stop counting at 5
"""for i in range(10):
    if i == 5:
        break
    print(i)"""

#Diamond problems/patterns help keep knowladge of programming there


n = int(input("Enter the size of the diamond: "))

for r in range(n):
    for c in range(1, n + 1):
        print(c, end='')
    print()






