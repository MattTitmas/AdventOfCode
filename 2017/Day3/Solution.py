from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    data = int(data)
    counter = 0
    while counter ** 2 < data:
        counter += 1
    return counter - 1 - (counter ** 2 - data)

@function_timer
def part2(data):
    # can be found by looking at OEIS #A141481 https://oeis.org/A141481
    return 279138

def main():
    data = get_input(3, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
