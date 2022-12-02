from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    data = list(map(lambda x: int(x), data.split('\t')))
    no_of_banks = len(data)

    seen = set(tuple(data))

    count = 0
    while True:
        count += 1
        max_index = int(max(range(len(data)), key=data.__getitem__))
        max_val = max(data)
        all_change = max_val // no_of_banks
        single_change = max_val - (no_of_banks * (max_val // no_of_banks))
        data[max_index] = 0
        if all_change > 0:
            for i in range(len(data)):
                data[i] += all_change
        for i in range(1, single_change + 1):
            data[(max_index + i) % len(data)] += 1

        if tuple(data) in seen:
            return count
        seen.add(tuple(data))


@function_timer_avg
def part2(data):
    data = list(map(lambda x: int(x), data.split('\t')))
    no_of_banks = len(data)

    seen = set(tuple(data))
    seen_at = {
        tuple(data): 0
    }

    count = 0
    while True:
        count += 1
        max_index = int(max(range(len(data)), key=data.__getitem__))
        max_val = max(data)
        all_change = max_val // no_of_banks
        single_change = max_val - (no_of_banks * (max_val // no_of_banks))
        data[max_index] = 0
        if all_change > 0:
            for i in range(len(data)):
                data[i] += all_change
        for i in range(1, single_change + 1):
            data[(max_index + i) % len(data)] += 1

        if tuple(data) in seen:
            return count - seen_at[tuple(data)]
        seen.add(tuple(data))
        seen_at[tuple(data)] = count


def main():
    data = get_input(6, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
