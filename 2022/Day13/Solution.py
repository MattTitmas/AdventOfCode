import json
from typing import List

from aoc import get_input
from utils import function_timer, function_timer_avg


def compare_packets(packet_one: List | int, packet_two: List | int, depth=0) -> int:
    for i, item in enumerate(packet_one):
        if i >= len(packet_two):
            return False
        first = item
        second = packet_two[i]
        if type(first) != type(second):
            if type(first) == int:
                first = [first]
            else:
                second = [second]
        if first == second:
            continue
        if type(first) == int:
            return True if first < second else False
        elif type(first) == list:
            temp = compare_packets(first, second)
            if temp is None:
                continue  # If they're equal (return value of None) then we must keep going.
            return temp
    return True if len(packet_one) < len(packet_two) else None



@function_timer
def part1(data):
    total = 0
    results = {}
    for count, packet_pair in enumerate(data.split('\n\n'), start=1):
        packet_one, packet_two = packet_pair.split('\n')
        right_order = compare_packets(json.loads(packet_one), json.loads(packet_two))
        if right_order:
            total += count
        results[right_order] = results.get(right_order, 0) + 1
    return total


@function_timer
def part2(data):
    total_before_two = 1
    total_before_six = 2
    for count, packet_pair in enumerate(data.split('\n\n'), start=1):
        for packet in packet_pair.split('\n'):
            if compare_packets(json.loads(packet), [[2]]):
                total_before_two += 1
                total_before_six += 1
            elif compare_packets(json.loads(packet), [[6]]):
                total_before_six += 1

    print(total_before_six, total_before_two)
    return total_before_six * total_before_two


def main():
    data = get_input(13, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
