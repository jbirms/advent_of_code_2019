#!/usr/bin/env python

"""
PLS WRITE DOCUMENTATION
"""

import argparse
from copy import deepcopy


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


def part2(input_code):
    desired_output = 19690720
    numbers = [int(i) for i in input_code.split(',')]

    # this brute-force solution feels gross, sorry mom
    for noun in range(100):
        for verb in range(100):
            numbers_copy = deepcopy(numbers)
            numbers_copy[1] = noun
            numbers_copy[2] = verb
            try:
                for i in range(0, len(numbers_copy), 4):
                    OP_CODES[numbers_copy[i]](numbers_copy, i)
            except Halt:
                if numbers_copy[0] == desired_output:
                    print("noun: {}, verb: {}, answer: {}".format(noun, verb, 100 * noun + verb))
                    return

            if numbers_copy[0] == desired_output:
                print("noun: {}, verb: {}, answer: {}".format(noun, verb, 100 * noun + verb))
                return
    print("found no matches :(")


def part1(input_code):
    numbers = [int(i) for i in input_code.split(',')]
    try:
        for i in range(0, len(numbers), 4):
            OP_CODES[numbers[i]](numbers, i)
    except Halt:
        print("halted, idx 0 = {}".format(numbers[0]))
        return

    print("halted, idx 0 = {}".format(numbers[0]))


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_code", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    part2(**vars(parse()))
