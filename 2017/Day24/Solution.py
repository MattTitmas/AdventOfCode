from collections import defaultdict

from aoc import get_input
from utils import function_timer_avg, function_timer


def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from gen_bridges(new, components)


@function_timer
def part1(data):
    components = defaultdict(set)
    for line in data.split('\n'):
        a, b = [int(x) for x in line.split('/')]
        components[a].add(b)
        components[b].add(a)

    max_strength = 0
    for bridge in gen_bridges(None, components):
        max_strength = max(max_strength, sum([sum(i) for i in bridge]))
    return max_strength


@function_timer
def part2(data):
    components = defaultdict(set)
    for line in data.split('\n'):
        a, b = [int(x) for x in line.split('/')]
        components[a].add(b)
        components[b].add(a)

    max_strength, max_len = 0, 0
    for bridge in gen_bridges(None, components):
        if len(bridge) == max_len:
            max_len = len(bridge)
            max_strength = max(max_strength, sum([sum(i) for i in bridge]))
        if len(bridge) > max_len:
            max_len = len(bridge)
            max_strength = sum([sum(i) for i in bridge])
    return max_strength


def main():
    data = get_input(24, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
