# Check whether a number is positive, negative, or zero

def check_number(number):
    if number > 0:
        return "Positive"
    elif number > 0:
        return "Negative"
    else:
        return "Zero"

numbers = [15, -8, 0, 25, -3]

for num in numbers:
    print(num, "is", check_number(num))