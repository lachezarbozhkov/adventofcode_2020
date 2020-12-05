from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def read_input():
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def get_parts(data):
    return data[:7], data[7:10]


def partition_row(row):
    return int(row.replace("F", "0").replace("B", "1"), 2)


def partition_seat(seat):
    return int(seat.replace("L", "0").replace("R", "1"), 2)


def id(row, seat):
    return row * 8 + seat


def test_functions():
    assert partition_row("FFFFFFF") == 0
    assert partition_row("BBBBBBB") == 127
    assert partition_row("FBFBBFF") == 44
    assert partition_row("BFFFBBF") == 70
    assert partition_row("FFFBBBF") == 14
    assert partition_row("BBFFBBF") == 102

    assert partition_seat("LLL") == 0
    assert partition_seat("RRR") == 7
    assert partition_seat("RLR") == 5
    assert partition_seat("RLL") == 4

    assert id(44, 5) == 357


def get_seat_ids(data):
    seats = []
    for line in data:
        row_code, seat_code = get_parts(line)
        row = partition_row(row_code)
        seat = partition_seat(seat_code)
        seat_id = id(row, seat)
        seats.append(seat_id)
    return seats


def find_missing(seats):
    seats = sorted(seats)
    previous = -1
    for i, seat_id in enumerate(seats):
        if previous != seat_id - 1:
            print("Missing seat number:", seat_id - 1)
            print(seats[i - 3 : i + 3])
        previous = seat_id


if __name__ == "__main__":
    print("## --- Solution ---\n")
    test_functions()
    data = read_input()
    seats = get_seat_ids(data)
    print("Max seat id:", max(seats))
    find_missing(seats)
