from pathlib import Path


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def parse_input(lines):
    lines = [line.split() for line in lines]
    return lines


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests
    lines = read_input()
    # print(lines)

    previous = 25
    for i in range(previous, len(lines)):
        temp_lines = lines[i - previous : i]
        current_number = int(lines[i])
        # print(current_number, temp_lines)
        number_ok = False
        for j in range(len(temp_lines)):
            for k in range(j + 1, len(temp_lines)):
                sum_numbers = int(temp_lines[k]) + int(temp_lines[j])
                number_ok = (sum_numbers == current_number) or number_ok
                if number_ok:
                    break
            if number_ok:
                break

        if number_ok is False:
            print("!!! Number not ok")
            print(i, current_number)
            index_number = i
            break

    print(index_number, current_number)

    lines = [int(line) for line in lines]
    for i in range(index_number):
        for j in range(i + 1, index_number):
            if sum(lines[i:j]) == current_number:
                print("This", i, j, sum(lines[i:j]))
                print(min(lines[i:j]) + max(lines[i:j]))
                exit()
        # else:
        #     print("Number ok!")
        #     print(i, lines[i])
