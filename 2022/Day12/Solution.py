from aoc import get_input
from utils import function_timer, function_timer_avg


def bfs(height_map, starting_pos, end_pos, return_path=False):
    to_explore = [starting_pos]
    explored = {starting_pos}
    distances = {starting_pos: 0}
    parents = {starting_pos: None}
    while len(to_explore) != 0:
        searching_x, searching_y = to_explore.pop(0)
        if (searching_x, searching_y) == end_pos:
            if not return_path:
                return distances[(searching_x, searching_y)]
            path = [(searching_x, searching_y)]
            current = (searching_x, searching_y)
            while parents[current] is not None:
                current = parents[current]
                path.append(current)
            return distances[(searching_x, searching_y)], path[::-1]

        for neighbour in get_neighbours_part1(height_map, (searching_x, searching_y)):
            if neighbour not in explored:
                explored.add(neighbour)
                distances[neighbour] = distances[(searching_x, searching_y)] + 1
                to_explore.append(neighbour)
                parents[neighbour] = (searching_x, searching_y)


def get_neighbours_part1(height_map, current_pos):
    rows = len(height_map)
    cols = len(height_map[0])
    x, y = current_pos
    neighbours = []
    if y - 1 >= 0 and height_map[y - 1][x] <= height_map[y][x] + 1:
        neighbours.append((x, y - 1))
    if y + 1 < rows and height_map[y + 1][x] <= height_map[y][x] + 1:
        neighbours.append((x, y + 1))
    if x - 1 >= 0 and height_map[y][x - 1] <= height_map[y][x] + 1:
        neighbours.append((x - 1, y))
    if x + 1 < cols and height_map[y][x + 1] <= height_map[y][x] + 1:
        neighbours.append((x + 1, y))

    return neighbours

def get_neighbours_part2(height_map, current_pos):
    rows = len(height_map)
    cols = len(height_map[0])
    x, y = current_pos
    neighbours = []
    if y - 1 >= 0 and height_map[y - 1][x] in range(height_map[y][x]-1, 27):
        neighbours.append((x, y - 1))
    if y + 1 < rows and height_map[y + 1][x] in range(height_map[y][x]-1, 27):
        neighbours.append((x, y + 1))
    if x - 1 >= 0 and height_map[y][x - 1] in range(height_map[y][x]-1, 27):
        neighbours.append((x - 1, y))
    if x + 1 < cols and height_map[y][x + 1] in range(height_map[y][x]-1, 27):
        neighbours.append((x + 1, y))

    return neighbours



@function_timer_avg
def part1(data):
    height_map = []
    starting_pos, end_pos = (-1, -1), (-1, -1)
    for count, i in enumerate(data.split('\n')):
        to_append = [ord(i) - 97 if (i != 'S' and i != 'E') else (0 if i == 'S' else 25) for i in list(i)]
        height_map.append(to_append)
        if 'S' in list(i):
            starting_pos = (list(i).index('S'), count)
        if 'E' in list(i):
            end_pos = (list(i).index('E'), count)

    to_explore = [starting_pos]
    explored = {starting_pos}
    distances = {starting_pos: 0}
    parents = {starting_pos: None}
    while len(to_explore) != 0:
        searching_x, searching_y = to_explore.pop(0)
        if (searching_x, searching_y) == end_pos:
            return distances[(searching_x, searching_y)]


        for neighbour in get_neighbours_part1(height_map, (searching_x, searching_y)):
            if neighbour not in explored:
                explored.add(neighbour)
                distances[neighbour] = distances[(searching_x, searching_y)] + 1
                to_explore.append(neighbour)
                parents[neighbour] = (searching_x, searching_y)


@function_timer
def part2(data):
    height_map = []
    starting_pos, end_pos = (-1, -1), (-1, -1)
    for count, i in enumerate(data.split('\n')):
        to_append = [ord(i) - 97 if (i != 'S' and i != 'E') else (0 if i == 'S' else 25) for i in list(i)]
        height_map.append(to_append)
        if 'E' in list(i):
            starting_pos = (list(i).index('E'), count)

    to_explore = [starting_pos]
    explored = {starting_pos}
    distances = {starting_pos: 0}
    parents = {starting_pos: None}
    while len(to_explore) != 0:
        searching_x, searching_y = to_explore.pop(0)
        if height_map[searching_y][searching_x] == 0:
            return distances[(searching_x, searching_y)]

        for neighbour in get_neighbours_part2(height_map, (searching_x, searching_y)):
            if neighbour not in explored:
                explored.add(neighbour)
                distances[neighbour] = distances[(searching_x, searching_y)] + 1
                to_explore.append(neighbour)
                parents[neighbour] = (searching_x, searching_y)

def main():
    data = get_input(12, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
