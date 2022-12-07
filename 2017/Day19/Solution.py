from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer
def part1(data):
    graph = []
    for i in data.split('\n'):
        row = list(i)
        graph.append(row)
    current_position = [0, 0]
    for count, i in enumerate(graph[0]):
        if i == '|':
            current_position = [0, count]
            break

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    stored = ''
    can_move, direction = True, 'south'
    while can_move:
        if graph[current_position[0]][current_position[1]] == 'U':
            return stored
        if direction == 'south':
            next_square = graph[current_position[0] + 1][current_position[1]]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[0] += 1
            elif next_square == '+':
                if graph[current_position[0] + 1][current_position[1] - 1] != ' ':
                    direction = 'west'
                else:
                    direction = 'east'
                current_position[0] += 1

        elif direction == 'north':
            next_square = graph[current_position[0] - 1][current_position[1]]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[0] -= 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] - 1] != ' ':
                    direction = 'west'
                else:
                    direction = 'east'
                current_position[0] -= 1

        elif direction == 'east':
            next_square = graph[current_position[0]][current_position[1] + 1]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[1] += 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] + 1] != ' ':
                    direction = 'north'
                else:
                    direction = 'south'
                current_position[1] += 1

        elif direction == 'west':
            next_square = graph[current_position[0]][current_position[1] - 1]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[1] -= 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] - 1] != ' ':
                    direction = 'north'
                else:
                    direction = 'south'
                current_position[1] -= 1

@function_timer
def part2(data):
    steps = 0
    graph = []
    for i in data.split('\n'):
        row = list(i)
        graph.append(row)
    current_position = [0, 0]
    for count, i in enumerate(graph[0]):
        if i == '|':
            current_position = [0, count]
            break

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    stored = ''
    can_move, direction = True, 'south'
    while can_move:
        steps += 1
        if graph[current_position[0]][current_position[1]] == 'U':
            return steps
        if direction == 'south':
            next_square = graph[current_position[0] + 1][current_position[1]]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[0] += 1
            elif next_square == '+':
                if graph[current_position[0] + 1][current_position[1] - 1] != ' ':
                    direction = 'west'
                else:
                    direction = 'east'
                current_position[0] += 1

        elif direction == 'north':
            next_square = graph[current_position[0] - 1][current_position[1]]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[0] -= 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] - 1] != ' ':
                    direction = 'west'
                else:
                    direction = 'east'
                current_position[0] -= 1

        elif direction == 'east':
            next_square = graph[current_position[0]][current_position[1] + 1]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[1] += 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] + 1] != ' ':
                    direction = 'north'
                else:
                    direction = 'south'
                current_position[1] += 1

        elif direction == 'west':
            next_square = graph[current_position[0]][current_position[1] - 1]
            if (next_square == '|') or (next_square == '-') or (next_square in alphabet):
                if next_square in alphabet:
                    stored += next_square
                current_position[1] -= 1
            elif next_square == '+':
                if graph[current_position[0] - 1][current_position[1] - 1] != ' ':
                    direction = 'north'
                else:
                    direction = 'south'
                current_position[1] -= 1


def main():
    data = get_input(19, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
