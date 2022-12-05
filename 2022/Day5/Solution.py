from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    starting_crates = data.split('\n\n')[0]
    commands = data.split('\n\n')[1]
    no_of_crates = int(max(starting_crates.split('\n')[-1].split('   ')))
    crates = [[] for i in range(no_of_crates)]
    for i in starting_crates.split('\n')[:-1]:
        for j in range(1, len(i), 4):
            if i[j] != ' ':
                crates[(j + 3) // ((len(i) + 1) // no_of_crates) - 1].insert(0, i[j])
    for command in commands.split('\n'):
        _, amount, _, tower_one, _, tower_two = command.split(' ')
        amount, tower_one, tower_two = int(amount), int(tower_one) - 1, int(tower_two) - 1
        for i in range(amount):
            crates[tower_two].append(crates[tower_one].pop(-1))

    return "".join([i[-1] for i in crates])

@function_timer_avg
def part2(data):
    starting_crates = data.split('\n\n')[0]
    commands = data.split('\n\n')[1]
    no_of_crates = int(max(starting_crates.split('\n')[-1].split('   ')))
    crates = [[] for i in range(no_of_crates)]
    for i in starting_crates.split('\n')[:-1]:
        for j in range(1, len(i), 4):
            if i[j] != ' ':
                crates[(j + 3) // ((len(i) + 1) // no_of_crates) - 1].insert(0, i[j])
    for command in commands.split('\n'):
        _, amount, _, tower_one, _, tower_two = command.split(' ')
        amount, tower_one, tower_two = int(amount), int(tower_one) - 1, int(tower_two) - 1
        new_list = []
        for i in range(amount):
            new_list.append(crates[tower_one].pop(-1))
        crates[tower_two] += new_list[::-1]

    return "".join([i[-1] for i in crates])


def main():
    data = get_input(5, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
