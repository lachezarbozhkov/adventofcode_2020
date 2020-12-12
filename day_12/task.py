from math import cos, radians, sin
from pathlib import Path


def read_input(file_name="input.txt"):
    input_path = Path(__file__).parent / file_name
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def task1(lines, verbose=False):
    # North (N): 0° = 360°
    # East (E): 90°
    # South (S): 180°
    # West (W): 270°
    north = 0
    east = 0
    direction = 90

    for line in lines:
        # Normalize degrees
        direction = (direction % 360 + 360) % 360

        operation = line[0]
        value = int(line[1:])
        if verbose:
            print((operation, value, direction))

        # Get direction in degrees
        if operation == "L":
            direction -= value
            continue  # Only change direction, no movement
        elif operation == "R":
            direction += value
            continue  # Only change direction, no movement

        # Move
        if operation == "N":
            north += value
        elif operation == "E":
            east += value
        elif operation == "S":
            north -= value
        elif operation == "W":
            east -= value
        elif operation == "F":
            travel_north = round(cos(radians(direction)), 2) * value
            travel_east = round(sin(radians(direction)), 2) * value
            north += travel_north
            east += travel_east
            if verbose:
                print(f"Travel forward: {travel_north}, travel east: {travel_east}")
        else:
            raise ValueError(f"Unknown direction: {operation}")

        if verbose:
            print("Position:", north, east)

    return round(abs(east) + abs(north))  # Manhattan distance


def task2(lines, verbose=False):
    north = 0
    east = 0
    way_point_north = 1
    way_point_east = 10

    for line in lines:
        operation = line[0]
        value = int(line[1:])
        if verbose:
            print(
                "Operation, value:",
                (operation, value),
                "; Way point (E, N):",
                (round(way_point_east), round(way_point_north)),
            )

        # Rotate way point
        # Original way point is  units east and 4 units north of the ship.
        # R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units
        # south of the ship. The ship remains at its position.
        # Only change direction, no movement
        if operation == "L":

            value = (-value % 360 + 360) % 360
            rads = radians(value)
            temp_east = way_point_east * cos(rads) + way_point_north * sin(rads)
            temp_north = -way_point_east * sin(rads) + way_point_north * cos(rads)
            way_point_east = temp_east
            way_point_north = temp_north
            continue
        elif operation == "R":
            rads = radians(value)
            temp_east = way_point_east * cos(rads) + way_point_north * sin(rads)
            temp_north = -way_point_east * sin(rads) + way_point_north * cos(rads)
            way_point_east = temp_east
            way_point_north = temp_north
            continue  # Only change direction, no movement

        # Move waypoint
        elif operation == "N":
            way_point_north += value
        elif operation == "E":
            way_point_east += value
        elif operation == "S":
            way_point_north -= value
        elif operation == "W":
            way_point_east -= value

        # Move ship
        elif operation == "F":
            north += value * way_point_north
            east += value * way_point_east
        else:
            raise ValueError(f"Unknown direction: {operation}")

        if verbose:
            print("Position:", north, east)

    return round(abs(east) + abs(north))  # Manhattan distance


if __name__ == "__main__":
    print("## --- Solution ---")

    # Tests 1
    print("Test task 1:")
    lines = read_input("test.txt")
    result = task1(lines, verbose=True)
    print(result)

    # Tests 2
    print("\n\nTest task 2:")
    lines = read_input("test.txt")
    result = task2(lines, verbose=True)
    print(result)

    # Input
    print("\n\nInput task 1:")
    lines = read_input()
    result = task1(lines, verbose=False)
    print(result)

    print("\n\nInput task 2:")
    lines = read_input()
    result = task2(lines, verbose=False)
    print(result)
