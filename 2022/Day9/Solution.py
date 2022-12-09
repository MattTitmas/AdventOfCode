from aoc import get_input
from utils import function_timer, function_timer_avg


def follow(tail, head):
    if all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)]):
        return tail
    (tail_x, tail_y), (head_x, head_y) = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail


@function_timer
def part1(data):
    movement = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    tail_positions = set()
    head = [0, 0]
    tail = [0, 0]
    for command in data.split('\n'):
        direction, steps = command.split(' ')
        for _ in range(int(steps)):
            delta_x, delta_y = movement[direction]
            head = head[0] + delta_x, head[1] + delta_y
            tail = follow(tail, head)
            tail_positions.add(tuple(tail))
    return len(tail_positions)


@function_timer
def part2(data):
    movement = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    tail_positions = set()
    positions = [[0, 0] for i in range(10)]
    for command in data.split('\n'):
        direction, steps = command.split(' ')
        for _ in range(int(steps)):
            delta_x, delta_y = movement[direction]
            positions[0] = positions[0][0] + delta_x, positions[0][1] + delta_y
            for i in range(1, len(positions)):
                positions[i] = follow(positions[i], positions[i - 1])
            tail_positions.add(tuple(positions[-1]))
    return len(tail_positions)


def main():
    data = get_input(9, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
