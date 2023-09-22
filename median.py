"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
length_of_list = len(numbers)
if length_of_list%2!=0:
    middle = int((length_of_list+1)/2)
    print(numbers[middle-1])
else:
    middle = int(length_of_list /2)
    average_of_both_middle = (numbers[middle-1] + numbers[middle])/2
    print(average_of_both_middle)
