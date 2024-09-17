__all__ = ["bubble_sorter"]


def bubble_sorter(data):
    """Sorts a list of numbers using the bubble sort algorithm."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
