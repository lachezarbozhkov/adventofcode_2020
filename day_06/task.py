from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def read_input():
    with input_path.open() as f:
        lines = f.read().split("\n\n")
    return lines


if __name__ == "__main__":
    print("## --- Solution ---\n")
    groups = read_input()
    any_answered_yes = 0
    all_answered_yes = 0

    for group in groups:

        # Task 1 solution
        any_answered_yes += len(set("".join(group.split("\n"))))

        sets = []
        for person in group.split():
            sets.append(set(person))

        ala = set.intersection(*sets)
        all_answered_yes += len(ala)

    print("Anyone answered yes:", any_answered_yes, end="\n\n")
    print("Everyone answered yes:", all_answered_yes)
