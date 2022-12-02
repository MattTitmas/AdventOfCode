from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    possible_roots = set()
    has_parent = set()
    for _data in data.split('\n'):
        name, rest = _data.split(' (')
        possible_roots.add(name)
        if '->' not in _data:
            continue
        children = rest.split('-> ')[1].split(', ')
        for i in children:
            has_parent.add(i)

    for _data in data.split('\n'):
        name, rest = _data.split(' (')
        if name not in has_parent:
            return name


def check_balanced(tree, weights, current):
    child_weights = dict()
    if not tree[current]:
        return weights[current], False

    for child in tree[current]:
        child_weights[child], complete = check_balanced(tree, weights, child)
        if complete:
            return child_weights[child], True

    if len(set(child_weights.values())) == 2:
        group_one = list(child_weights.values())[0]
        single = True
        for i in list(child_weights.values())[1:]:
            if i != group_one:
                group_two = i
            else:
                single = False
        problem_child = list(child_weights.keys())[list(child_weights.values()).index(group_one if single else group_two)]
        wanted_weight = group_two if single else group_one
        actual_weight = group_one if single else group_two
        return weights[problem_child] + (wanted_weight - actual_weight), True

    return sum(child_weights.values()) + weights[current], False


@function_timer
def part2(data):
    root = 'gmcrj'
    weights = {
        i.split(' (')[0]: int(i.split('(')[1].split(')')[0]) for i in data.split('\n')
    }
    tree = {
        i.split(' (')[0]: i.split(' -> ')[1].split(', ') if '->' in i else [] for i in data.split('\n')
    }
    return check_balanced(tree, weights, root)


def main():
    data = get_input(7, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)[0]}')


if __name__ == '__main__':
    main()
