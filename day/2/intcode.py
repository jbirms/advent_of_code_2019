#!/usr/bin/env python

"""
PLS WRITE DOCUMENTATION
"""

import argparse


class Halt(Exception):
    pass


def add_next_two_indices(full_list, starting_position):
    """
    :param full_list: full list of numbers, edited in place
    :param starting_position: should correspond to the index of the 1 op_code
    """
    full_list[full_list[starting_position + 3]] = (full_list[full_list[starting_position + 1]]
                                                   + full_list[full_list[starting_position + 2]])


def multiply_next_two_indices(full_list, starting_position):
    """
    :param full_list: full list of numbers, edited in place
    :param starting_position: should correspond to the index of the 2 op_code
    """
    full_list[full_list[starting_position + 3]] = (full_list[full_list[starting_position + 1]]
                                                   * full_list[full_list[starting_position + 2]])


def fail_expectedly(*_):
    raise Halt


OP_CODES = {
    1: add_next_two_indices,
    2: multiply_next_two_indices,
    99: fail_expectedly
}


def main(input_code):
    numbers = [int(i) for i in input_code.split(',')]
    try:
        for i in range(0, len(numbers), 4):
            OP_CODES[numbers[i]](numbers, i)
    except Halt:
        print("full numbers: [{}]".format(",".join([str(i) for i in numbers])))
        print("halted, idx 0 = {}".format(numbers[0]))
        return

    print("full numbers: [{}]".format(",".join([str(i) for i in numbers])))
    print("halted, idx 0 = {}".format(numbers[0]))


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_code", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    main(**vars(parse()))
