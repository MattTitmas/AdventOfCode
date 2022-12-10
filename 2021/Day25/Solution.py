from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [list(i) for i in data.split("\n")]
    colLen = len(values)
    rowLen = len(values[0])
    prev = [["" for j in row] for row in values]
    count = 0
    while True:
        count += 1
        copy = [row[:] for row in values]
        # East Facing
        for i in range(len(copy)):
            for j in range(len(copy[i])):
                if copy[i][(j + 1) % rowLen] == "." and copy[i][j] == ">":
                    values[i][j % rowLen] = "."
                    values[i][(j + 1) % rowLen] = ">"
        copy = [row[:] for row in values]
        # South Facing
        for i in range(len(copy)):
            for j in range(len(copy[i])):
                if copy[(i+1) % colLen][j] == "." and copy[i][j] == "v":
                    values[i % colLen][j] = "."
                    values[(i+1) % colLen][j] = "v"
        allMatching = True
        for i in range(len(values)):
            for j in range(len(values[i])):
                if prev[i][j] != values[i][j]:
                    allMatching = False
        if allMatching:
            return count
        prev = [row[:] for row in values]

@function_timer_avg
def part2(data):
    return 0
def main():
    data = get_input(25, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
