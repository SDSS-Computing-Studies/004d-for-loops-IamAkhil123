#! python3

list_1 = [25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99]

result = list (filter (lambda x: (x % 5 == 0), list_1))

print("Numbers that are divisible by 5 are:", result)


"""
##### Task 3
Given a typle that contains a series of numbers, list all the ones that are
divisible by 5
(2 points)

inputs:
none

outputs:
list of numbers
25
10
30
75
20
"""

numList = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)