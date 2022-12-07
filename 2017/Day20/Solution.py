import numpy as np

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    closest = 0
    min_acc, min_vel, min_pos = float('inf'), float('inf'), float('inf')
    for count, i in enumerate(data.split('\n')):
        position = sum([abs(int(i)) for i in i.split(', ')[0][3:-1].split(',')])
        velocity = sum([abs(int(i)) for i in i.split(', ')[1][3:-1].split(',')])
        acceleration = sum([abs(int(i)) for i in i.split(', ')[2][3:-1].split(',')])
        if acceleration < min_acc:
            min_acc = acceleration
            closest = count
        elif acceleration == min_acc:
            if velocity < min_vel:
                min_vel = velocity
                closest = count
            elif velocity == min_vel:
                if position < min_pos:
                    min_pos = position
                    closest = count
    return closest


@function_timer
def part2(data):
    positions = np.array([[int(j) for j in i.split(', ')[0][3:-1].split(',')] for i in data.split('\n')])
    velocity = np.array([[int(j) for j in i.split(', ')[1][3:-1].split(',')] for i in data.split('\n')])
    acceleration = np.array([[int(j) for j in i.split(', ')[2][3:-1].split(',')] for i in data.split('\n')])

    previous_dist = []
    while True:
        velocity += acceleration
        positions += velocity

        seen = set()
        duplicates = set()
        for i in positions:
            if tuple(i) in seen:
                duplicates.add(tuple(i))
            seen.add(tuple(i))
        to_remove = []
        for count, i in enumerate(positions):
            if tuple(i) in duplicates:
                to_remove.append(count)

        mask = np.ones(len(positions), dtype=bool)
        mask[to_remove] = False
        positions = positions[mask]
        velocity = velocity[mask]
        acceleration = acceleration[mask]

        position_a = np.repeat(positions, len(positions), axis=0)
        position_b = np.tile(positions, (len(positions), 1))
        dist = np.linalg.norm(position_a - position_b, axis=1)

        if len(dist) != len(previous_dist):
            previous_dist = dist
        else:
            if np.greater_equal(dist, previous_dist).all():
                return len(positions)
            previous_dist = dist

def main():
    data = get_input(20, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
