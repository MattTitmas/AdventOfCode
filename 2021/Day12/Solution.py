from aoc import get_input
from utils import function_timer_avg, function_timer


def find_all_paths(graph, start, end, costs, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if costs[node] != 0:
                costs[node] -= 1
                newpaths = find_all_paths(graph, node, end, costs, path)
                for newpath in newpaths:
                    paths.append(newpath)
                costs[node] += 1
        return paths 


@function_timer_avg
def part1(data):
    values = [i.split("-") for i in data.split("\n")]
    graph = {}
    cost = {}
    for path in values:
        cost[path[0]] = (-5 if path[0].upper() == path[0] else 1) if path[0] not in cost else cost[path[0]]
        cost[path[1]] = (-5 if path[1].upper() == path[1] else 1) if path[1] not in cost else cost[path[1]]
        if path[0] in graph:
            graph[path[0]].append(path[1])
        else:
            graph[path[0]] = [path[1]]
        if path[1] in graph:
            graph[path[1]].append(path[0])
        else:
            graph[path[1]] = [path[0]]
    cost['start'] = 0
    return len(find_all_paths(graph,'start','end', cost))

@function_timer_avg
def part2(data):
    values = [i.split("-") for i in data.split("\n")]
    graph = {}
    cost = {}
    for path in values:
        cost[path[0]] = (-5 if path[0].upper() == path[0] else 1) if path[0] not in cost else cost[path[0]]
        cost[path[1]] = (-5 if path[1].upper() == path[1] else 1) if path[1] not in cost else cost[path[1]]
        if path[0] in graph:
            graph[path[0]].append(path[1])
        else:
            graph[path[0]] = [path[1]]
        if path[1] in graph:
            graph[path[1]].append(path[0])
        else:
            graph[path[1]] = [path[0]]
    cost['start'] = 0
    paths = set()
    for key in graph.keys():
        if cost[key] == 1:
            cost[key] = 2
        test = find_all_paths(graph,'start','end',cost)
        for path in test:
            paths.add(tuple(path))
        if cost[key] == 2:
            cost[key] = 1
    return len(paths)

def main():
    data = get_input(12, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
    
