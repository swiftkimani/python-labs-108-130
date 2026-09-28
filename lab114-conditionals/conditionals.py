# Lab 114 - Conditionals
# AWS re/Start - Python Programming

# Simple if statement
age = 20
if age >= 18:
    print("You are an adult")

# if / else
temperature = 15
if temperature > 25:
    print("It is warm")
else:
    print("It is cool")

# if / elif / else
score = 87
print("\nScore is", score)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade is", grade)

# Comparison operators
a = 10
b = 5
print("\nComparison operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical operators
print("\nLogical operators")
has_id = True
print("age >= 18 and has_id :", age >= 18 and has_id)
print("age < 18 or has_id   :", age < 18 or has_id)
print("not has_id           :", not has_id)

# Nested conditionals
print("\nNested conditionals")
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")

# Checking membership with in
print("\nMembership")
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("apple is in the list")

if "mango" not in fruits:
    print("mango is not in the list")

# Conditional expression (ternary)
print("\nConditional expression")
result = "pass" if score >= 75 else "fail"
print("Result:", result)

# Checking for an empty value
print("\nEmpty values are False")
items = []
if items:
    print("The list has items")
else:
    print("The list is empty")

# Checking a number range
print("\nRange check")
number = 45
if 0 <= number <= 100:
    print(number, "is between 0 and 100")
