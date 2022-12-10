from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [[int(j) for j in list(i)] for i in data.split("\n")]
    total = 0
    for x in range(len(values)):
        for y in range(len(values[x])):
            minimum_point = True
            for i in range(max(0, x - 1), min(x + 2, 100)):
                for j in range(max(0, y - 1), min(y + 2, 100)):
                    if abs(x - i) != abs(y - j):
                        minimum_point = (minimum_point and (values[i][j] > values[x][y]))

            if minimum_point:
                total += 1 + (values[x][y])
    return total


def flood_fill(values, x, y):
    if x < 0 or y < 0 or x > 99 or y > 99:
        return 0
    if values[x][y] == -1 or values[x][y] == 9:
        return 0
    total = 1
    values[x][y] = -1
    total += flood_fill(values, x - 1, y)
    total += flood_fill(values, x + 1, y)
    total += flood_fill(values, x, y - 1)
    total += flood_fill(values, x, y + 1)

    return total


@function_timer_avg
def part2(data):
    values = [[int(j) for j in list(i)] for i in data.split("\n")]
    maxThree = []
    for x in range(len(values)):
        for y in range(len(values[x])):
            minimum_point = True
            for i in range(max(0, x - 1), min(x + 2, 100)):
                for j in range(max(0, y - 1), min(y + 2, 100)):
                    if abs(x - i) != abs(y - j):
                        minimum_point = (minimum_point and (values[i][j] > values[x][y]))
            if minimum_point:
                value = (flood_fill(values, x, y))
                if len(maxThree) != 3:
                    maxThree.append(value)
                else:
                    if value > min(maxThree):
                        maxThree[maxThree.index(min(maxThree))] = value
    return maxThree[0] * maxThree[1] * maxThree[2]


def main():
    data = get_input(9, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
