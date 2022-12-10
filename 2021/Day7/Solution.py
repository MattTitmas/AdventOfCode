from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [int(i) for i in data.split(",")]
    maximum = max(values)
    finalCost = float("inf")
    for i in range(maximum):
        totalCost = 0
        for cost in values:
            totalCost += abs(cost - i)
        if totalCost < finalCost:
            finalCost = totalCost
        else:
            return finalCost


@function_timer_avg
def part2(data):
    values = [int(i) for i in data.split(",")]
    maximum = max(values)
    finalCost = float("inf")
    for i in range(maximum):
        totalCost = 0
        for cost in values:
            distance = abs(cost - i)
            totalCost += (distance * (distance + 1)) / 2
        if totalCost < finalCost:
            finalCost = totalCost
        else:
            return int(finalCost)


def main():
    data = get_input(7, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
