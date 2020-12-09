from pathlib import Path


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def task_1(lines, previous):
    for i in range(previous, len(lines)):
        previous_lines = lines[i - previous : i]
        current_number = lines[i]
        is_valid = False

        for j in range(len(previous_lines)):  # Iterate through all possible lines
            # k & j will try all possible previous numbers combinations
            for k in range(j + 1, len(previous_lines)):
                is_valid = current_number == (previous_lines[k] + previous_lines[j])
                if is_valid:
                    break
            if is_valid:
                break

        if is_valid is False:
            return i, current_number

    return -1, "All valid numbers"


def task_2(lines, index_number):
    for i in range(index_number):
        for j in range(i + 1, index_number):
            if sum(lines[i:j]) == lines[index_number]:
                return min(lines[i:j]) + max(lines[i:j])


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests
    lines = read_input("test.txt")
    lines = [int(line) for line in lines]
    previous = 5
    index_number, number = task_1(lines, previous)
    assert number == 127
    assert index_number == 14

    min_plus_max = task_2(lines, index_number)
    assert min_plus_max == 62

    # Real input
    lines = read_input()
    lines = [int(line) for line in lines]

    # Task 1
    previous = 25
    index_number, number = task_1(lines, previous)
    print("Task 1 index:", index_number, "number:", number)

    min_plus_max = task_2(lines, index_number)
    print("Task 2:", min_plus_max)
