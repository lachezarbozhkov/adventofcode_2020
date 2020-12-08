from pathlib import Path


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def parse_input(lines):
    lines = [line.split() for line in lines]
    return lines


def program(lines):
    index = 0
    accumulator = 0
    executed_commands = set()

    while index < len(lines):
        if index in executed_commands:
            return False, accumulator
        executed_commands.add(index)

        operation = lines[index][0]
        value = int(lines[index][1])
        if operation == "jmp":
            index += value
            continue
        elif operation == "acc":
            accumulator += value

        index += 1

    return True, accumulator


def fix_error(lines):
    for i, line in enumerate(lines):
        lines_2 = [line.copy() for line in lines]
        if line[0] == "jmp":
            lines_2[i][0] = "nop"
        elif line[0] == "nop":
            lines_2[i][0] = "jmp"
        else:
            continue

        finished, accumulator = program(lines_2)
        if finished:
            return finished, i, accumulator

    return False, None, None


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests
    lines = read_input("test.txt")
    lines = parse_input(lines)
    # Task 1
    finished, accumulator = program(lines)
    assert finished is False
    assert accumulator == 5
    # Task 2
    finished, i, accumulator = fix_error(lines)
    assert finished
    assert accumulator == 8

    # Input
    lines = read_input()
    lines = parse_input(lines)
    # Task 1
    finished, accumulator = program(lines)
    print("Task 1:", finished, accumulator)
    # Task 2
    finished, i, accumulator = fix_error(lines)
    print("Task 2:", finished, i, accumulator)
