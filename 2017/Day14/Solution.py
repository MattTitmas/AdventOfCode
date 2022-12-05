from utils import knot_hash

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    total = 0
    for i in range(0, 128):
        bin_hash = bin(int(knot_hash(data + '-' + str(i)), 16))[2:].zfill(128)
        total += sum(list(map(int, list(bin_hash))))
    return total


@function_timer
def part2(data):
    count = 0
    unseen = []
    for i in range(0, 128):
        bin_hash = bin(int(knot_hash(data + '-' + str(i)), 16))[2:].zfill(128)
        unseen += [(i, j) for j, d in enumerate(bin_hash) if d == '1']
    while len(unseen) != 0:
        to_check = [unseen[0]]
        while len(to_check) > 0:
            x, y = to_check.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                to_check += [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        count += 1
    return count


def main():
    data = get_input(14, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
