"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
if len(numbers) % 2 == 0:
    temp = len(numbers) / (len(numbers) + 1)
    print(numbers[temp])
else:
    print(numbers[len(numbers) + 1])

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
