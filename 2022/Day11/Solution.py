from aoc import get_input
from utils import function_timer, function_timer_avg


def update_monkeys(monkeys, inspections, div=0):
    for i in range(len(monkeys)):
        (items, operation, test, true_throw, false_throw) = monkeys[i]
        while len(items) > 0:
            inspections[i] += 1
            current_item = items.pop(0)
            val_1 = (current_item if operation[0] == 'old' else int(operation[0]))
            val_2 = (current_item if operation[2] == 'old' else int(operation[2]))
            new_val = (val_1 * val_2 if operation[1] == '*' else val_1 + val_2)
            if div == 0:
                new_val = new_val // 3
            else:
                new_val = new_val % div
            if new_val % test:
                monkeys[false_throw][0] = monkeys[false_throw][0] + [new_val]
            else:
                monkeys[true_throw][0] = monkeys[true_throw][0] + [new_val]
    return monkeys, inspections

@function_timer
def part1(data):
    split_data = data.split('\n')
    monkeys = dict()
    for i in range(0, len(split_data), 7):
        monkey_number = int(split_data[i].split(' ')[1][:-1])
        items = [int(i) for i in split_data[i + 1].split(': ')[-1].split(', ')]
        operation = [int(i) if i.isnumeric() else i for i in "".join(split_data[i + 2].split(' = ')[-1]).split(' ')]
        test = int(split_data[i + 3].split(' ')[-1])
        true_throw = int(split_data[i + 4].split(' ')[-1])
        false_throw = int(split_data[i + 5].split(' ')[-1])
        monkeys[monkey_number] = [items, operation, test, true_throw, false_throw]
    inspections = [0 for i in monkeys]
    for _ in range(20):
        monkeys, inspections = update_monkeys(monkeys, inspections)
    maximum = max(inspections)
    inspections.remove(maximum)
    second_max = max(inspections)

    return maximum * second_max


@function_timer
def part2(data):
    split_data = data.split('\n')
    monkeys = dict()
    total_divisors = 1
    for i in range(0, len(split_data), 7):
        monkey_number = int(split_data[i].split(' ')[1][:-1])
        items = [int(i) for i in split_data[i + 1].split(': ')[-1].split(', ')]
        operation = [int(i) if i.isnumeric() else i for i in "".join(split_data[i + 2].split(' = ')[-1]).split(' ')]
        test = int(split_data[i + 3].split(' ')[-1])
        true_throw = int(split_data[i + 4].split(' ')[-1])
        false_throw = int(split_data[i + 5].split(' ')[-1])
        monkeys[monkey_number] = [items, operation, test, true_throw, false_throw]
        total_divisors *= test
    inspections = [0 for i in monkeys]
    seen, first_seen, order= set(), dict(), ()
    previously_seen = 0
    for j in range(10000):
        monkeys, inspections = update_monkeys(monkeys, inspections, div=total_divisors)
        order = tuple(tuple(monkeys[i][0]) for i in monkeys)
        if order in seen:
            previously_seen = j
            break
        seen.add(order)
        first_seen[order] = j
    if first_seen[order] != 9999:
        inspections_in_loop = [0 for i in monkeys]
        for i in range(previously_seen - first_seen[order]):
            monkeys, inspections_in_loop = update_monkeys(monkeys, inspections_in_loop, div=total_divisors)
        inspection_factor = ((10000 - 184) // 90)
        for i in range(len(inspections_in_loop)):
            inspections_in_loop[i] *= inspection_factor
            inspections_in_loop[i] += inspections[i]
        for i in range(inspection_factor * (previously_seen - first_seen[order]) + 185, 10000):
            monkeys, inspections_in_loop = update_monkeys(monkeys, inspections_in_loop, div=total_divisors)
        maximum = max(inspections_in_loop)
        inspections_in_loop.remove(maximum)
        second_max = max(inspections_in_loop)
    else:
        maximum = max(inspections)
        inspections.remove(maximum)
        second_max = max(inspections)
    return maximum * second_max


def main():
    data = get_input(11, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
