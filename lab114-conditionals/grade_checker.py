# Lab 114 - Conditionals
# Grade checker with input validation

score = input("Enter a score between 0 and 100: ")

# Check the input is a number before converting it
if not score.isdigit():
    print("That is not a valid whole number")
else:
    score = int(score)

    if score < 0 or score > 100:
        print("The score must be between 0 and 100")
    elif score >= 90:
        print("Grade A - Excellent")
    elif score >= 80:
        print("Grade B - Very good")
    elif score >= 70:
        print("Grade C - Good")
    elif score >= 60:
        print("Grade D - Pass")
    else:
        print("Grade F - Needs improvement")
