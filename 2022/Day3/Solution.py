from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    priority = 0
    for line in data.split('\n'):
        first, second = line[:len(line) // 2], line[len(line) // 2:]
        common_letter = next(iter(set(first).intersection(set(second))))
        ord_common = ord(common_letter)
        if ord_common >= 97:
            priority += ord_common - 96
        else:
            priority += ord_common - 38
    return priority



@function_timer_avg
def part2(data):
    priority = 0
    split_data = data.split('\n')
    for i in range(2, len(split_data), 3):
        set_one, set_two, set_three = set(split_data[i-2]), set(split_data[i-1]), set(split_data[i])
        ord_common = ord(next(iter(set_three.intersection(set_two).intersection(set_one))))

        if ord_common >= 97:
            priority += ord_common - 96
        else:
            priority += ord_common - 38
    return priority


def main():
    data = get_input(3, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
