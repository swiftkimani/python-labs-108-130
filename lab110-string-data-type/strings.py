# Lab 110 - String Data Type
# AWS re/Start - Python Programming

message = "Amazon Web Services"

# Length and indexing
print("message =", message)
print("length  =", len(message))
print("first character =", message[0])
print("last character  =", message[-1])

# Slicing
print("\nSlicing")
print("message[0:6]  =", message[0:6])
print("message[7:10] =", message[7:10])
print("message[11:]  =", message[11:])
print("message[::-1] =", message[::-1])

# String methods
print("\nString methods")
print("upper()      =", message.upper())
print("lower()      =", message.lower())
print("title()      =", message.title())
print("replace()    =", message.replace("Amazon", "AWS"))
print("split()      =", message.split())
print("count('e')   =", message.count("e"))
print("find('Web')  =", message.find("Web"))
print("startswith() =", message.startswith("Amazon"))
print("endswith()   =", message.endswith("Services"))

# Stripping whitespace
spaced = "   extra spaces   "
print("\nstrip() =", spaced.strip())

# Concatenation and repetition
first = "Hello"
second = "World"
print("\nConcatenation =", first + " " + second)
print("Repetition    =", first * 3)

# Joining a list into a string
words = ["Amazon", "Web", "Services"]
print("join()        =", " ".join(words))

# Formatting output
name = "Benard"
labs = 17
print("\nFormatted output")
print(f"{name} has completed {labs} labs")
print("{} has completed {} labs".format(name, labs))

# Checking what a string contains
print("\nString tests")
print("'abc'.isalpha()  =", "abc".isalpha())
print("'123'.isdigit()  =", "123".isdigit())
print("'abc1'.isalnum() =", "abc1".isalnum())
