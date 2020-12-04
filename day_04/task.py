import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def read_input():
    with input_path.open() as f:
        lines = f.read().split("\n\n")  # Passports are sep by an empty line
    return lines


def validate_keys_in_data(passports):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    counter = len(passports)
    for passports in passports:
        for key in keys:
            if key not in passports:
                counter -= 1
                break

    return counter


def validate_passports(passports):
    counter = 0
    for passport in passports:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        pattern = re.compile(r"byr:(\d{4})\b")
        match = re.search(pattern, passport)
        if not match:
            continue
        match_date = int(match.groups()[0])
        if match_date < 1920 or match_date > 2002:
            continue

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        pattern = re.compile(r"iyr:(\d{4})\b")
        match = re.search(pattern, passport)
        if not match:
            continue
        match_date = int(match.groups()[0])
        if match_date < 2010 or match_date > 2020:
            continue

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        pattern = re.compile(r"eyr:(\d{4})\b")
        match = re.search(pattern, passport)
        if not match:
            continue
        match_date = int(match.groups()[0])
        if match_date < 2020 or match_date > 2030:
            continue

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.

        pattern = re.compile(r"hgt:(\d+)(cm|in)\b")
        match = re.search(pattern, passport)
        if not match:
            continue
        hgt = int(match.groups()[0])
        hgt_unit = match.groups()[1]
        if hgt_unit == "cm" and (hgt < 150 or hgt > 193):
            continue
        elif hgt_unit == "in" and (hgt < 59 or hgt > 76):
            continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        pattern = re.compile(r"hcl:#([\d|a-f]{6})\b")
        match = re.search(pattern, passport)
        if not match:
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

        pattern = re.compile(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b")
        match = re.search(pattern, passport)
        if not match:
            continue

        # pid (passports ID) - a nine-digit number, including leading zeroes.

        pattern = re.compile(r"pid:(\d{9})\b")
        match = re.search(pattern, passport)
        if not match:
            continue

        # cid (Country ID) - ignored, missing or not.

        counter += 1
    return counter


if __name__ == "__main__":
    print("## --- Solution ---\n")
    text = read_input()
    passports = text

    print(f"{len(passports)} passports.", end="\n\n\n")
    print("Passport data:")
    print(passports[0], end="\n\n\n")

    print("Valid passports task 1:", validate_keys_in_data(passports))

    print("Valid passports task 2:", validate_passports(passports))
