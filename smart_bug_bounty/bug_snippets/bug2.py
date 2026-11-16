
def get_last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        return []

    if n == 0:
        return []

    if n > len(items):
        return items

    # BUG: The slice excludes the final element.
    return items[-n:-1]


numbers = [10, 20, 30, 40, 50]
result = get_last_items(numbers, 3)
print("Last items:", result)