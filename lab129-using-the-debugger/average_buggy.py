# Lab 129 - Using the Debugger
# AWS re/Start - Python Programming
#
# This program should print the average of the scores, which is 89.0
# but it prints something else. Use the debugger to find out why.
#
#   python3 -m pdb average_buggy.py

scores = [88, 92, 79, 95, 91]


def calculate_average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total = total + number
        count = 1            # this is the bug - it should be count = count + 1

    return total / count


def find_highest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest


print("Scores:", scores)
print("Average:", calculate_average(scores))
print("Highest:", find_highest(scores))
print("\nExpected average: 89.0")
