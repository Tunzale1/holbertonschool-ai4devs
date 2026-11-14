def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / (len(numbers) - 1)
    return average


scores = [80, 90, 70, 100]
print("Average:", calculate_average(scores))