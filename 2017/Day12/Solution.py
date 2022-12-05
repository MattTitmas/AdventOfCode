import networkx as nx

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    connections = {int(i.split(' <-> ')[0]): tuple([int(j) for j in i.split(' <-> ')[1].split(', ')]) for i in data.split('\n')}
    to_check = [0]
    seen = set()
    while len(to_check) > 0:
        checking = to_check.pop(0)
        seen.add(checking)
        for i in connections[checking]:
            if i not in seen:
                to_check.append(i)
    return len(seen)


@function_timer_avg
def part2(data):
    graph = nx.Graph()
    for connection in data.split('\n'):
        node, neighbours = connection.split(' <-> ')
        graph.add_edges_from((node, neighbour) for neighbour in neighbours.split(', '))
    return nx.number_connected_components(graph)

def main():
    data = get_input(12, 2017)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
