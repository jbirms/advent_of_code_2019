#!/usr/bin/env python

"""
day 4
"""

import argparse


def parse_num_range(num_range):
    """
    input format example: 147368-234566

    :type num_range: str
    :rtype: int, int
    """
    # it'd be better to validate/parse with regexes here
    return int(num_range[:6]), int(num_range[7:13])


def is_valid_password(password):
    """
    A password is valid if:
        - Two adjacent digits are the same (like 22 in 122345).
        - Going from left to right, the digits never decrease;
            they only ever increase or stay the same (like 111123 or 135679).

        part 2 - new rule!
        - there needs to be at least 1 group of only 2 adjacent numbers

    :type password: int
    :rtype: bool
    """
    digits = [int(c) for c in str(password)]
    adjacent_group_sizes = set()
    most_recent_group_size = 1
    for i, digit in enumerate(digits):
        if i == 0:
            continue  # easiest way to avoid off-by-one errors
        if digit < digits[i - 1]:
            return False
        elif digit == digits[i - 1]:
            most_recent_group_size += 1
        else:
            adjacent_group_sizes.add(most_recent_group_size)
            most_recent_group_size = 1
    return (2 in adjacent_group_sizes) or (most_recent_group_size == 2)


def main(num_range):
    range_min, range_max = parse_num_range(num_range)
    num_valid_passwords = 0
    for i in range(range_min, range_max):
        if is_valid_password(i):
            num_valid_passwords += 1
    print("found {} valid passwords".format(num_valid_passwords))


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("num_range", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    main(**vars(parse()))
