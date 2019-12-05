#!/usr/bin/env python

"""
day 1: calculating fuel requirements
"""

import argparse


def get_fuel_requirements(mass, running_total=0):
    initial_fuel_mass = mass // 3 - 2
    if initial_fuel_mass <= 0:
        return running_total
    else:
        return get_fuel_requirements(initial_fuel_mass, initial_fuel_mass + running_total)


def main(fuel_file):
    total = 0
    for line in fuel_file:
        mass = int(line.strip())
        total += get_fuel_requirements(mass)
    print("total mass = " + str(total))


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fuel_file", type=argparse.FileType('r'))
    return parser.parse_args()


if __name__ == "__main__":
    main(**vars(parse()))
