from src.hello_world.app import bubble_sorter


def test_bubble_sorter():
    items = [5, 3, 8, 6, 1, 9, 2]
    assert bubble_sorter(items) == [1, 2, 3, 5, 6, 8, 9]

test_bubble_sorter()