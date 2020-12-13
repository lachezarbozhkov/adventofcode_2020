from pathlib import Path

import numpy as np


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")

    array = np.array([list(line) for line in lines])
    return array


def task1(array_new, adjacent_fn):
    x, y = array_new.shape
    array = np.zeros_like(array_new)

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    # Floor (.) never changes; seats don't move, and nobody sits on the floor.

    while True:
        if (array == array_new).all():
            break  # Stable equilibrium achieved
        array = np.copy(array_new)
        # Calculate new array positions
        for i in range(x):
            for j in range(y):
                index = i, j
                adjacent = adjacent_fn(array, index)
                current = array[index]

                if current == ".":
                    continue
                elif current == "L" and (adjacent == "#").sum() == 0:
                    array_new[index] = "#"
                elif current == "#" and (adjacent == "#").sum() >= 5:
                    array_new[index] = "L"

    return (array_new == "#").sum()


def get_adjacent_1(array, index):
    x, y = array.shape
    i, j = index
    return array[max(i - 1, 0) : min(i + 2, x), max(j - 1, 0) : min(j + 2, y)]


def get_adjacent_2(array, index):
    x, y = array.shape
    i, j = index

    # N, NE, E, SE, S, SW, W, NW - directions

    N = "."
    for k in range(1, x):
        index = (i - k, j)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            N = array[index]
            break

    NE = "."
    for k in range(1, x):
        index = (i - k, j + k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            NE = array[index]
            break

    E = "."
    for k in range(1, x):
        index = (i, j + k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            E = array[index]
            break

    SE = "."
    for k in range(1, x):
        index = (i + k, j + k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            SE = array[index]
            break

    S = "."
    for k in range(1, x):
        index = (i + k, j)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            S = array[index]
            break

    SW = "."
    for k in range(1, x):
        index = (i + k, j - k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            SW = array[index]
            break

    W = "."
    for k in range(1, x):
        index = (i, j - k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            W = array[index]
            break

    NW = "."
    for k in range(1, x):
        index = (i - k, j - k)
        if index[0] >= x or index[0] < 0 or index[1] >= y or index[1] < 0:
            break
        if array[index] != ".":
            NW = array[index]
            break

    return np.array([[NW, N, NE], [W, None, E], [SW, S, SE]])


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests 1
    print("Test task 1:")
    lines = read_input("test.txt")
    result = task1(lines, adjacent_fn=get_adjacent_1)
    assert result == 37
    print(result)

    # # Tests 2
    adj = get_adjacent_2(read_input("test.adjacent_1.txt"), (4, 3))
    assert (adj == "#").sum() == 8
    adj = get_adjacent_2(read_input("test.adjacent_2.txt"), (3, 3))
    print(adj)
    assert (adj == ".").sum() == 8

    lines = read_input("test.txt")
    result = task1(lines, adjacent_fn=get_adjacent_2)
    print("\n\nTest task 2:")
    print(result)

    # Input
    print("\n\nInput task 1:")
    lines = read_input()
    result = task1(lines, get_adjacent_1)
    print(result)

    print("\n\nInput task 2:")
    lines = read_input()
    result = task1(lines, get_adjacent_2)
    print(result)
