#!/usr/bin/env python

"""
PLS WRITE DOCUMENTATION
"""


import argparse


def up(start):
    return start + Point(0, 1)


def down(start):
    return start + Point(0, -1)


def left(start):
    return start + Point(-1, 0)


def right(start):
    return start + Point(1, 0)


CHAR_TO_FUNC = {
    "U": up,
    "D": down,
    "L": left,
    "R": right
}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def manhattan_dist_from_origin(self):
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash(repr(self))


ORIGIN = Point(0, 0)

def parseline(line):
    current_loc = ORIGIN
    points = [current_loc]
    segments = line.split(',')
    for segment in segments:
        func = CHAR_TO_FUNC[segment[0]]
        magnitude = int(segment[1:])
        for i in range(magnitude):
            new_loc = func(current_loc)
            points.append(new_loc)
            current_loc = new_loc
    return points


def main(line1, line2):
    line1_points = parseline(line1)
    line2_points = parseline(line2)
    line1_set = set(line1_points)
    print("finished parsing the lines")
    intersection_lengths = []
    for i, point in enumerate(line2_points):
        if point != ORIGIN and point in line1_set:
            intersection_lengths.append(line1_points.index(point) + i)
    print("min length: {}".format(min(intersection_lengths)))


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--line1", type=str)
    parser.add_argument("--line2", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    main(**vars(parse()))
