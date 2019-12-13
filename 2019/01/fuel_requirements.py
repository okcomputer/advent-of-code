#!/usr/bin/env python
import math

FUEL_TOTAL = 0


def main(input_file=None):
    """
    Take file with list of fuel mass
    """
    with open(input_file) as data:
        lines = data.read().splitlines()
    return lines


def get_fuel_req(mass):
    """
    """
    div_floor = math.floor(int(mass) / 3) - 2
    if div_floor > 0:
        return div_floor + get_fuel_req(div_floor)
    return 0


if __name__ == "__main__":
    puzzle_input = main(input_file="puzzle_input.txt")
    for fuel_mass in puzzle_input:
        FUEL_TOTAL += get_fuel_req(fuel_mass)
    print(FUEL_TOTAL)
