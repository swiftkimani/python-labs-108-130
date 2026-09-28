# Lab 115 - Loops
# Print a multiplication table using nested loops

number = int(input("Enter a number for the times table: "))

print(f"\nMultiplication table for {number}")
print("-" * 25)

for i in range(1, 13):
    print(f"{number} x {i:2} = {number * i}")
