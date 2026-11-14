def get_last_items(items, n):
    if n < 0:
        return []

    return items[-n:-1]


numbers = [10, 20, 30, 40, 50]
print(get_last_items(numbers, 3))