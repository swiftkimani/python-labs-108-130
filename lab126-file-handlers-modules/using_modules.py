# Lab 126 - File Handlers and Modules
# Using modules from the Python standard library

import math
import random
import os
import sys
from datetime import datetime

# math
print("MATH MODULE")
print("math.pi       =", round(math.pi, 4))
print("math.sqrt(16) =", math.sqrt(16))
print("math.ceil(4.2)=", math.ceil(4.2))
print("math.floor(4.8)=", math.floor(4.8))
print("math.pow(2, 8)=", math.pow(2, 8))

# random
print("\nRANDOM MODULE")
random.seed(1)   # seeding makes the results repeatable
print("randint(1, 100) =", random.randint(1, 100))
print("choice           =", random.choice(["A", "C", "G", "T"]))
print("sample           =", random.sample(range(1, 50), 5))

# datetime
print("\nDATETIME MODULE")
now = datetime.now()
print("Now:", now.strftime("%Y-%m-%d %H:%M"))
print("Year:", now.year)

# os
print("\nOS MODULE")
print("Current directory:", os.getcwd())
print("Files here:", len(os.listdir(".")))

# sys
print("\nSYS MODULE")
print("Python version:", sys.version.split()[0])
print("Platform:", sys.platform)

# Different ways to import
print("\nIMPORT STYLES")
print("import math            -> math.sqrt(9) =", math.sqrt(9))

from math import sqrt
print("from math import sqrt  -> sqrt(9) =", sqrt(9))

import math as m
print("import math as m       -> m.sqrt(9) =", m.sqrt(9))
