from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    # X, A -> Rock
    # Y, B -> Paper
    # Z, C -> Scissors
    points = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
              ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
              ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}
    total_score = 0
    for i in data.split('\n'):
        their, yours = i.split(' ')
        total_score += points[(their, yours)]
    return total_score




@function_timer_avg
def part2(data):
    # A, B, C = Rock (1), Paper (2), Scissors (3)
    # X, Y, Z = Lose (0), Draw (3), Win (6)
    points = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
              ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
              ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7,}
    total_score = 0
    for i in data.split('\n'):
        their, yours = i.split(' ')
        total_score += points[(their, yours)]
    return total_score


def main():
    data = get_input(2, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
