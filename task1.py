#!python3 

num = int(input("enter the number"))
print(num)
i = 2
timer = 0 
while timer<=10:
    y = num * i
    print(y)
    i = i + 2
    timer = timer + 1
"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""
