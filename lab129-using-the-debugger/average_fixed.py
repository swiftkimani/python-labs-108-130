# Lab 129 - Using the Debugger
# The corrected version

scores = [88, 92, 79, 95, 91]


def calculate_average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total = total + number
        count = count + 1    # fixed - the counter now increases each time

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
