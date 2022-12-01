from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    checksum = 0
    for i in data.split('\n'):
        values = list(map(lambda x: int(x), i.split('\t')))
        checksum += max(values) - min(values)
    return checksum


@function_timer_avg
def part2(data):
    checksum = 0
    for i in data.split('\n'):
        values = list(map(lambda x: int(x), i.split('\t')))
        for a in range(len(values)):
            for b in range(len(values)):
                if a == b:
                    continue
                if values[a] % values[b] == 0:
                    checksum += values[a] // values[b]
    return checksum


def main():
    data = get_input(2, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
