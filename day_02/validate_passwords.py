import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
PASSWORD_PATTERN = re.compile(r"^(\d+)-(\d+) ([a-zA-Z]): (\w+)$")


def read_input():
    with input_path.open() as f:
        lines = f.read().splitlines()
    return lines


def parse_line(line):
    match = re.match(PASSWORD_PATTERN, line)
    min_char, max_char, char, password = match.groups()
    min_char, max_char = int(min_char), int(max_char)
    return min_char, max_char, char, password


def check_policy_one(min_char, max_char, char, password):
    len_chars = sum([c == char for c in password])
    return min_char <= len_chars and max_char >= len_chars


def check_policy_two(min_char, max_char, char, password):
    correctness = int(password[min_char - 1] == char)
    correctness += int(password[max_char - 1] == char)
    return correctness == 1


if __name__ == "__main__":
    lines = read_input()
    print("## --- Solution ---\n")
    print("Number of lines:", len(lines))

    correct_policy_one = sum([check_policy_one(*parse_line(line)) for line in lines])
    print("Correct for policy one:", correct_policy_one)
    print()

    correct_policy_two = sum([check_policy_two(*parse_line(line)) for line in lines])
    print("Correct for policy two:", correct_policy_two)
