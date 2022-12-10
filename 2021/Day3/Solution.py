from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [int(i) for i in data.split("\n")]
    count = [0] * len(values[0])

    for i in values:
        for c, char in enumerate(i):
            count[c] += int(char)

    gamma = 0
    epsilon = 0

    for i in count:
        gamma *= 2
        epsilon *= 2
        if i >= len(values) / 2:
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon


@function_timer_avg
def part2(data):
    oxygen = [i for i in data.split("\n")]
    co2 = [i for i in data.split("\n")]

    for count in range(12):
        mostCommonOxygen = 0
        mostCommonCo2 = 0
        for c, val in enumerate(oxygen):
            mostCommonOxygen += int(val[count])
        for c, val in enumerate(co2):
            mostCommonCo2 += int(val[count])
        mostCommonOxygen = 1 if mostCommonOxygen >= len(oxygen) / 2 else 0
        mostCommonCo2 = 1 if mostCommonCo2 >= len(co2) / 2 else 0

        toDeleteOxygen = []
        for c, val in enumerate(oxygen):
            if int(val[count]) != mostCommonOxygen:
                toDeleteOxygen.append(c)
        for i in range(len(toDeleteOxygen) - 1, -1, -1):
            del oxygen[toDeleteOxygen[i]]

        toDeleteCo2 = []
        for c, val in enumerate(co2):
            if int(val[count]) == mostCommonCo2:
                toDeleteCo2.append(c)

        if len(co2) != 1:
            for i in range(len(toDeleteCo2) - 1, -1, -1):
                del co2[toDeleteCo2[i]]

    return int(oxygen[0], 2) * int(co2[0], 2)


def main():
    data = get_input(3, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
