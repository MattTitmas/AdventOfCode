import numpy as np

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    commands = dict()
    for i in data.split('\n'):
        start, end = i.split(' => ')
        end = tuple(tuple([1 if k == '#' else 0 for k in i]) for i in end.split('/'))
        start, start_flip = tuple(tuple([1 if k == '#' else 0 for k in i]) for i in start.split('/')), tuple(
            tuple([1 if k == '#' else 0 for k in i])[::-1] for i in start.split('/'))
        commands[start] = end
        commands[start_flip] = end
        for _ in range(3):
            start, start_flip = tuple(zip(*start[::-1])), tuple(zip(*start_flip[::-1]))
            commands[start] = end
            commands[start_flip] = end

    current_state = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])

    for i in range(5):
        new_state_dict = dict()
        if len(current_state) % 2 == 0:
            diff = 2
        else:
            diff = 3
        max_j, max_k = 0, 0
        for j in range(0, len(current_state), diff):
            for k in range(0, len(current_state), diff):
                B = current_state[j:j + diff, k:k + diff]
                tupled = tuple(tuple(chunk) for chunk in B)
                max_j, max_k = j, k
                new_state_dict[(max_j, max_k)] = commands[tupled]
        new_state = None
        for j in range(0, max_j + 1, diff):
            temp = None
            for k in range(0, max_k + 1, diff):
                if temp is None:
                    temp = np.array(new_state_dict[(j, k)])
                else:
                    temp = np.hstack((temp, np.array(new_state_dict[(j, k)])))
            new_state = temp if new_state is None else np.vstack((new_state, temp))
        current_state = new_state
    return np.sum(current_state)


@function_timer
def part2(data):
    commands = dict()
    for i in data.split('\n'):
        start, end = i.split(' => ')
        end = tuple(tuple([1 if k == '#' else 0 for k in i]) for i in end.split('/'))
        start, start_flip = tuple(tuple([1 if k == '#' else 0 for k in i]) for i in start.split('/')), tuple(
            tuple([1 if k == '#' else 0 for k in i])[::-1] for i in start.split('/'))
        commands[start] = end
        commands[start_flip] = end
        for _ in range(3):
            start, start_flip = tuple(zip(*start[::-1])), tuple(zip(*start_flip[::-1]))
            commands[start] = end
            commands[start_flip] = end

    current_state = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])

    for i in range(18):
        new_state_dict = dict()
        if len(current_state) % 2 == 0:
            diff = 2
        else:
            diff = 3
        max_j, max_k = 0, 0
        for j in range(0, len(current_state), diff):
            for k in range(0, len(current_state), diff):
                B = current_state[j:j + diff, k:k + diff]
                tupled = tuple(tuple(chunk) for chunk in B)
                max_j, max_k = j, k
                new_state_dict[(max_j, max_k)] = commands[tupled]
        new_state = None
        for j in range(0, max_j + 1, diff):
            temp = None
            for k in range(0, max_k + 1, diff):
                if temp is None:
                    temp = np.array(new_state_dict[(j, k)])
                else:
                    temp = np.hstack((temp, np.array(new_state_dict[(j, k)])))
            new_state = temp if new_state is None else np.vstack((new_state, temp))
        current_state = new_state
    return np.sum(current_state)


def main():
    data = get_input(21, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
