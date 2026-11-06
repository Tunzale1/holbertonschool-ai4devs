# Calculate the average of a list of numbers

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


values = [10, 20, 30, 40]
assert calculate_average(values) == 25.0
assert calculate_average([5, 10, 15]) == 10.0

print("Bug 1 fixed successfully!")
print("Average:", calculate_average(values))