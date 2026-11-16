
def get_last_items(items, n):
    if n <= 0:
        return []

    return items[-n:]


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("Last items:", get_last_items(numbers, 3))