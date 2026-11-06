# Check whether a number is positive, negative, or zero

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


assert check_number(15) == "Positive"
assert check_number(-8) == "Negative"
assert check_number(0) == "Zero"

numbers = [15, -8, 0, 25, -3]

for num in numbers:
    print(num, "is", check_number(num))

print("Bug 2 fixed successfully!")