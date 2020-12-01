from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with input_path.open() as f:
    lines = f.read().splitlines()


# Task 1
def check_sum_2020(numbers):
    numbers = [int(n) for n in numbers]
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(i + 1, len_numbers):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i], numbers[j]

    raise Exception("No numbers sum up to 2020!")


# Task 2
def check_sum_2020_three_numbers(numbers):
    numbers = [int(n) for n in numbers]
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(i + 1, len_numbers):
            for k in range(j + 1, len_numbers):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i], numbers[j], numbers[k]

    raise Exception("No 3 numbers sum up to 2020!")


number_1, number_2 = check_sum_2020(lines)
print(number_1, "*", number_2, "Product =", number_1 * number_2)

number_1, number_2, number_3 = check_sum_2020_three_numbers(lines)
print(
    number_1, "*", number_2, "*", number_3, "Product =", number_1 * number_2 * number_3
)
