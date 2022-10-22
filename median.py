"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
a = list()

if len(a)%2==0:
    temp=len(a)/(len(a)+1)
    print(list[temp])
else:
    print(list[len(a)+1])

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
