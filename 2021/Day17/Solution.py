from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [[int(j) for j in i.split("=")[1].split("..")] for i in data.split(": ")[1].split(", ")]
    for i in range(len(values)):
        values[i] = list(range(values[i][0], values[i][1]+1))

    minX, maxX = min(values[0]), max(values[0])
    minY, maxY = min(values[1]), max(values[1])
    toReturn = float("-inf")
    for x in range(0, maxX+1):
        for y in range(-(minY-1), minY-1, -1):
            overShot = False
            hit = False
            position = [0, 0]
            velocity = [x, y]
            highestY = float("-inf")
            while not overShot and not hit:
                position[0] += velocity[0]
                position[1] += velocity[1]
                highestY = max(highestY, position[1])
                velocity[0] += (-1 if velocity[0] > 0 else (1 if velocity[0] < 0 else 0))
                velocity[1] -= 1
                if position[0] > maxX or position[1] < minY:
                    overShot = True
                elif maxX >= position[0] >= minX and maxY >= position[1] >= minY:
                    toReturn = max(highestY, toReturn)
                    hit = True
    return toReturn


@function_timer_avg
def part2(data):
    values = [[int(j) for j in i.split("=")[1].split("..")] for i in data.split(": ")[1].split(", ")]
    for i in range(len(values)):
        values[i] = list(range(values[i][0], values[i][1]+1))

    minX, maxX = min(values[0]), max(values[0])
    minY, maxY = min(values[1]), max(values[1])

    total = 0
    for x in range(0, maxX+1):
        for y in range(-(minY-1), minY-1, -1):
            overShot = False
            hit = False
            position = [0, 0]
            velocity = [x, y]
            while not overShot and not hit:
                position[0] += velocity[0]
                position[1] += velocity[1]
                velocity[0] += (-1 if velocity[0] > 0 else (1 if velocity[0] < 0 else 0))
                velocity[1] -= 1
                if position[0] > maxX or position[1] < minY:
                    overShot = True
                elif maxX >= position[0] >= minX and maxY >= position[1] >= minY:
                    total += 1
                    hit = True
    return total



def main():
    data = get_input(17, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
