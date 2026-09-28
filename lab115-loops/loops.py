# Lab 115 - Loops
# AWS re/Start - Python Programming

# ----- FOR LOOP -----
print("FOR LOOP")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string
print("\nLooping through a string")
for letter in "Python":
    print(letter, end=" ")
print()

# Using range()
print("\nUsing range()")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print()

print("range(0, 20, 5):", end=" ")
for i in range(0, 20, 5):
    print(i, end=" ")
print()

print("counting down:", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Using enumerate to get the index as well
print("\nUsing enumerate()")
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Looping through two lists with zip
print("\nUsing zip()")
names = ["Benard", "Asha"]
cohorts = ["KENAI52", "KENAI51"]
for name, cohort in zip(names, cohorts):
    print(name, "is in", cohort)

# Looping through a dictionary
print("\nLooping through a dictionary")
student = {"name": "Benard", "cohort": "KENAI52", "labs": 17}
for key, value in student.items():
    print(key, "=", value)

# ----- WHILE LOOP -----
print("\nWHILE LOOP")
count = 5
while count > 0:
    print(count, end=" ")
    count = count - 1
print("Liftoff!")

# ----- BREAK AND CONTINUE -----
print("\nBREAK - stop the loop early")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("\nCONTINUE - skip this pass")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# ----- NESTED LOOPS -----
print("\nNESTED LOOPS - times table")
for row in range(1, 5):
    for col in range(1, 5):
        print(f"{row * col:4}", end="")
    print()

# ----- ACCUMULATING IN A LOOP -----
print("\nAdding up numbers in a loop")
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total = total + number
print("Total =", total)

print("\nCounting items that match a condition")
scores = [88, 45, 92, 67, 79]
passed = 0
for score in scores:
    if score >= 70:
        passed = passed + 1
print(passed, "out of", len(scores), "passed")

# ----- LIST COMPREHENSION -----
print("\nList comprehension")
squares = [n * n for n in range(1, 6)]
print("squares =", squares)

evens = [n for n in range(1, 11) if n % 2 == 0]
print("evens =", evens)
