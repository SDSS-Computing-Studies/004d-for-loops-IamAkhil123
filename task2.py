#! python3

List = ("Lebron", "Kobe", "Michale", "Shaq", "Dennis")
x = input("Enter a name")
for i in List:
 if i == x:
  print("That name is in the list")
  break
else:
  print("That name is not on the list")


"""
while True:
 x = input("Enter your name")
 if x == List:
  print("That name is in the list")
 else:
  print("That name is not on the list")
"""
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. 
Use a for loop this time instead of a single if with multiple logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""

