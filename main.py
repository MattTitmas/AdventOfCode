from utils.timer import Timer
from AdventOfCode2017.Solutions import *
from __init__ import ROOT

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run code for a specific day of Advent Of Code 2017."
    )
    parser.add_argument("--part1", action="store_false")
    parser.add_argument("--part2", action="store_false")
    parser.add_argument("-year", type=str, required=True, help="year to run")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-day", type=int, help="day to run")
    group.add_argument("--allDays", action="store_true")

    args = parser.parse_args()
    if not args.allDays:
        input_path = str(
            ROOT
            / (
                "Advent of code/AdventOfCode"
                + str(args.year)
                + "/Inputs/input"
                + str(args.day)
                + ".txt"
            )
        )
        day = Day1(input_path)
        exec("day = Day" + str(args.day) + "(input_path)")
        if args.part1:
            print(f"Part1: {day.part1}")
        if args.part2:
            print(f"Part2: {day.part2}")
    else:
        for i in range(25):
            print(f"Day {i+1}:")
            currentDay = i + 1
            input_path = str(
                ROOT
                / (
                    "Advent of Code/AdventOfCode2017/Inputs/input"
                    + str(currentDay)
                    + ".txt"
                )
            )
            day = Day1(input_path)
            exec("day = Day" + str(currentDay) + "(input_path)")
            if args.part1:
                print(f"\tPart1: {day.part1}")
            if args.part2:
                print(f"\tPart2: {day.part2}")
