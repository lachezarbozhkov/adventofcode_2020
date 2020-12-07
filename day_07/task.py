from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def read_input():
    with input_path.open() as f:
        lines = f.read().split("\n")
    return lines


def split_bags(line):
    out_bag, inner_bags = line.split(" contain ")
    out_bag = out_bag[:-1]

    return out_bag, inner_bags
    # inner_bags = inner_bags.split(", ")

    # shiny cyan bags contain 5 faded violet bags, 3 mirrored bronze bags, 4 dark maroon bags, 2 wavy lavender bags.


def inner_bag(line):
    outter, inner = split_bags(line)
    return inner


def fix_bag_naming(text):
    # '2 dark red bags', '1 dull green bag.'
    if text == "no other bags.":
        return text
    if text[-1] == ".":
        text = text[:-1]
    if text[-1] == "s":
        text = text[:-1]

    return text


def search_1(lines):
    queue = [line for line in lines if "shiny gold bag" in inner_bag(line)]
    used = {"shiny gold bag"}
    while queue:
        line = queue.pop()
        outter, inner = split_bags(line)
        if outter in used:
            continue

        new_queue = [line for line in lines if outter in inner_bag(line)]
        used.add(outter)
        queue += new_queue
    return used


def search_2(bag_color: str, bags: dict, verbose=True):
    other_bags = [fix_bag_naming(bag) for bag in bags[bag_color].split(", ")]

    if verbose:
        print("bag_color:", other_bags)

    counter = 1
    for bag in other_bags:
        if bag == "no other bags.":
            return 1

        bag_count = int(bag[:1])  # Get the number of this type of bag
        bag_name = bag[2:]  # Get the bag name without number
        counter += bag_count * search_2(bag_name, bags, verbose)

    return counter


test_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

if __name__ == "__main__":
    print("## --- Solution ---")
    lines = read_input()

    # Task 1
    # Test
    assert len(search_1(test_1.splitlines())) - 1 == 4

    # Task
    used = search_1(lines)
    print("Task 1:", len(used) - 1)

    # TASK 2
    # Test
    result = (split_bags(line) for line in test_2.splitlines())
    bags = {outter: inner for outter, inner in result}
    count_of_bags = search_2("shiny gold bag", bags, verbose=False)
    assert count_of_bags - 1 == 126

    # Task
    result = (split_bags(line) for line in lines)
    bags = {outter: inner for outter, inner in result}

    counter = search_2("shiny gold bag", bags, verbose=False)
    print("Task 2:", counter - 1)
