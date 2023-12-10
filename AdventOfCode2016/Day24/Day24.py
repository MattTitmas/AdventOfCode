from collections import deque
from itertools import permutations


def distance(graph, val1, val2):
    seen = set()
    queue = deque([(val1, 0)])
    maxDistance = 1000
    while queue:
        node, distance = queue.popleft()
        if node in seen or maxDistance < distance:
            continue
        seen.add(node)
        if node == val2:
            return distance
        xPos = node[0]
        yPos = node[1]
        if graph[xPos - 1][yPos] != "#":
            queue.append(((xPos - 1, yPos), distance + 1))
        if graph[xPos + 1][yPos] != "#":
            queue.append(((xPos + 1, yPos), distance + 1))
        if graph[xPos][yPos - 1] != "#":
            queue.append(((xPos, yPos - 1), distance + 1))
        if graph[xPos][yPos + 1] != "#":
            queue.append(((xPos, yPos + 1), distance + 1))


def part1():
    graph = [list(i) for i in open("input.txt", "r").read().split("\n")]
    locationOfNos = {
        0: (17, 149),
        1: (25, 149),
        2: (35, 159),
        3: (3, 147),
        4: (3, 9),
        5: (17, 9),
        6: (11, 143),
        7: (29, 39),
    }
    distanceBetweenNos = {}
    for key, value in locationOfNos.items():
        for keyComp, valueComp in locationOfNos.items():
            if keyComp != key:
                if tuple(sorted((key, keyComp))) not in distanceBetweenNos:
                    distanceBetweenNos[tuple(sorted((key, keyComp)))] = distance(
                        graph, locationOfNos[key], locationOfNos[keyComp]
                    )
    minDist = float("inf")
    for i in permutations([1, 2, 3, 4, 5, 6, 7]):
        perm = [0] + list(i)
        currentDist = 0
        for j in range(0, len(perm) - 1):
            currentDist += distanceBetweenNos[tuple(sorted((perm[j], perm[j + 1])))]
        minDist = min(currentDist, minDist)
    return minDist


def part2():
    graph = [list(i) for i in open("input.txt", "r").read().split("\n")]
    locationOfNos = {
        0: (17, 149),
        1: (25, 149),
        2: (35, 159),
        3: (3, 147),
        4: (3, 9),
        5: (17, 9),
        6: (11, 143),
        7: (29, 39),
    }
    distanceBetweenNos = {}
    for key, value in locationOfNos.items():
        for keyComp, valueComp in locationOfNos.items():
            if keyComp != key:
                if tuple(sorted((key, keyComp))) not in distanceBetweenNos:
                    distanceBetweenNos[tuple(sorted((key, keyComp)))] = distance(
                        graph, locationOfNos[key], locationOfNos[keyComp]
                    )
    minDist = float("inf")
    for i in permutations([1, 2, 3, 4, 5, 6, 7]):
        perm = [0] + list(i) + [0]
        currentDist = 0
        for j in range(0, len(perm) - 1):
            currentDist += distanceBetweenNos[tuple(sorted((perm[j], perm[j + 1])))]
        minDist = min(currentDist, minDist)
    return minDist


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")
