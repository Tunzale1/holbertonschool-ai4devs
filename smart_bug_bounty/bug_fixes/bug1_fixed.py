
def calculate_average(numbers):
    if not numbers:
        return 0

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    return average


if __name__ == "__main__":
    scores = [80, 90, 70, 100]
    print("Average:", calculate_average(scores))