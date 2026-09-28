# Lab 111 - List, Tuple, Dictionary
# AWS re/Start - Python Programming

# ----- LIST -----
# Ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]
print("LIST")
print("fruits =", fruits)
print("fruits[0] =", fruits[0])
print("length =", len(fruits))

fruits.append("orange")
print("after append:", fruits)

fruits.insert(1, "mango")
print("after insert:", fruits)

fruits.remove("banana")
print("after remove:", fruits)

last = fruits.pop()
print("after pop:", fruits, "- removed", last)

fruits.sort()
print("after sort:", fruits)

fruits.reverse()
print("after reverse:", fruits)

# ----- TUPLE -----
# Ordered, NOT changeable, allows duplicates
print("\nTUPLE")
coordinates = (10, 20)
print("coordinates =", coordinates)
print("coordinates[0] =", coordinates[0])

# A tuple cannot be changed
try:
    coordinates[0] = 99
except TypeError as error:
    print("Error when changing a tuple:", error)

# Unpacking a tuple
x, y = coordinates
print("x =", x, "and y =", y)

# A tuple with one item needs a comma
single = (5,)
print("single =", single, type(single))

# ----- DICTIONARY -----
# Key/value pairs, changeable, keys must be unique
print("\nDICTIONARY")
student = {
    "name": "Benard",
    "cohort": "KENAI52",
    "labs": 17
}
print("student =", student)
print("student['name'] =", student["name"])
print("get('email') =", student.get("email"))
print("get with default =", student.get("email", "not provided"))

student["email"] = "benard@example.com"
print("after adding email:", student)

student["labs"] = 20
print("after updating labs:", student)

del student["email"]
print("after delete:", student)

print("\nkeys   =", list(student.keys()))
print("values =", list(student.values()))
print("items  =", list(student.items()))

print("\nLooping through the dictionary")
for key, value in student.items():
    print(key, "->", value)

# ----- SET -----
# Unordered, no duplicates
print("\nSET")
numbers = {1, 2, 3, 3, 2, 1}
print("set removes duplicates:", numbers)
