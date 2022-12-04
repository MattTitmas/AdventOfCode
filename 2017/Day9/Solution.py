from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    current_depth, score = 0, 0
    in_garbage = False
    skipping = False
    for i in data:
        if skipping:
            skipping = False
            continue
        if i == '{' and not in_garbage:
            current_depth += 1
            continue
        elif i == '}' and not in_garbage:
            score += current_depth
            current_depth -= 1
        elif i == '<' and not in_garbage:
            in_garbage = True
            continue
        elif in_garbage:
            if i == '!':
                skipping = True
                continue
            if i == '>':
                in_garbage = False

    return score


@function_timer_avg
def part2(data):
    chars_in_garbage = 0
    in_garbage = False
    skipping = False
    for i in data:
        if skipping:
            skipping = False
            continue
        if i == '<' and not in_garbage:
            in_garbage = True
            continue
        if in_garbage:
            if i == '!':
                skipping = True
                continue
            if i == '>':
                in_garbage = False
            else:
                chars_in_garbage += 1
    return chars_in_garbage


def main():
    data = get_input(9, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
