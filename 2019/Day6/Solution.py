from typing import Dict, List

from aoc import get_input
from utils import function_timer_avg, function_timer


def orbits(orbit_graph: Dict[str, List[str]], root: str, depth = 1) -> int:
    no_of_orbits = 0
    if root not in orbit_graph:
        return 0
    for i in orbit_graph[root]:
        no_of_orbits += orbits(orbit_graph, i, depth+1) + depth
    return no_of_orbits


@function_timer
def part1(data):
    children = dict()
    possible_roots = set()
    for line in data.split('\n'):
        object_one, object_two = tuple(line.split(')'))

        children[object_one] = children.get(object_one, []) + [object_two]
        possible_roots.add(object_one)
    for line in data.split('\n'):
        object_one, object_two = tuple(line.split(')'))
        if object_two in possible_roots:
            possible_roots.remove(object_two)
    return orbits(children, next(iter(possible_roots)))



def bfs(orbit_graph, starting_pos, end_pos):
    to_explore = [starting_pos]
    explored = {starting_pos}
    distances = {starting_pos: 0}
    while len(to_explore) != 0:
        current = to_explore.pop(0)
        if current == end_pos:
            return distances[current]
        for edge in orbit_graph[current]:
            if edge not in explored:
                explored.add(edge)
                distances[edge] = distances[current] + 1
                to_explore.append(edge)


@function_timer
def part2(data):
    orbit_graph = {}
    for line in data.split('\n'):
        object_one, object_two = tuple(line.split(')'))
        orbit_graph[object_one] = orbit_graph.get(object_one, []) + [object_two]
        orbit_graph[object_two] = orbit_graph.get(object_two, []) + [object_one]
    return bfs(orbit_graph, 'YOU', 'SAN') - 2

def main():
    data = get_input(6, 2019)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
