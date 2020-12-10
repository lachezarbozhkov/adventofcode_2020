from collections import Counter
from pathlib import Path


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def task1(lines):
    difference = {1: 0, 2: 0, 3: 0}
    prev_jolt = 0
    for jolt in lines:
        diff = jolt - prev_jolt
        if diff > 3:
            return difference
        difference[diff] += 1
        prev_jolt = jolt

    return difference[1] * difference[3]


def task2(lines):
    counter = Counter()
    counter[0] = 1

    for line in lines:
        counter[line] = counter[line - 1] + counter[line - 2] + counter[line - 3]

    return counter[lines[-1]]


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests 1
    lines = read_input("test.txt")
    lines = sorted([int(line) for line in lines])
    lines.append(lines[-1] + 3)

    difference = task1(lines)
    assert difference == 35
    combinations = task2(lines)
    assert combinations == 8

    # Test 2
    lines = read_input("test2.txt")
    lines = sorted([int(line) for line in lines])
    lines.append(lines[-1] + 3)

    difference = task1(lines)
    assert difference == 220
    combinations = task2(lines)
    assert combinations == 19208

    # Input

    lines = read_input()
    lines = sorted([int(line) for line in lines])
    lines.append(lines[-1] + 3)

    difference = task1(lines)
    print("Task 1:", difference)

    combinations = task2(lines)
    print("Task 2:", combinations)
