from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def read_input():
    with input_path.open() as f:
        lines = f.read().splitlines()
    return lines


def calculate_path(lines, x, y):
    counter = 0
    right = 0
    for i in range(y, len(lines), y):
        line = lines[i]
        right += x
        if right >= len(line):
            right -= len(line)

        counter += line[right] == "#"
    return counter


if __name__ == "__main__":
    print("## --- Solution ---\n")

    lines = read_input()

    print("Number of lines:", len(lines))

    # Task 1
    print(calculate_path(lines, 3, 1))

    # Task 2
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    product = 1
    for x, y in paths:
        product = product * calculate_path(lines, x, y)

    print(product)
