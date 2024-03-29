import collections

from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [[1 if i.split(" ")[0] == "on" else 0, [[int(k) for k in j[2:].split("..")] for j in i.split(" ")[1].split(",")]] for i in data.split("\n")][:20]
    cubes = collections.Counter()
    for i in values:
        sign = i[0]
        x0, x1 = i[1][0]
        y0, y1 = i[1][1]
        z0, z1 = i[1][2]

        update = collections.Counter()

        for (ox0, ox1, oy0, oy1, oz0, oz1), osign in cubes.items():
            intersectx0 = max(x0, ox0)
            intersectx1 = min(x1, ox1)
            intersecty0 = max(y0, oy0)
            intersecty1 = min(y1, oy1)
            intersectz0 = max(z0, oz0)
            intersectz1 = min(z1, oz1)
            if intersectx0 <= intersectx1 and intersecty0 <= intersecty1 and intersectz0 <= intersectz1:
                update[(intersectx0, intersectx1, intersecty0, intersecty1, intersectz0, intersectz1)] -= osign
        if sign > 0:
            update[(x0, x1, y0, y1, z0, z1)] += sign
        cubes.update(update)

    return sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
               for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())

@function_timer_avg
def part2(data):
    values = [[1 if i.split(" ")[0] == "on" else 0, [[int(k) for k in j[2:].split("..")] for j in i.split(" ")[1].split(",")]] for i in data.split("\n")]
    cubes = collections.Counter()
    for i in values:
        sign = i[0]
        x0, x1 = i[1][0]
        y0, y1 = i[1][1]
        z0, z1 = i[1][2]

        update = collections.Counter()

        for (ox0, ox1, oy0, oy1, oz0, oz1), osign in cubes.items():
            intersectx0 = max(x0, ox0)
            intersectx1 = min(x1, ox1)
            intersecty0 = max(y0, oy0)
            intersecty1 = min(y1, oy1)
            intersectz0 = max(z0, oz0)
            intersectz1 = min(z1, oz1)
            if intersectx0 <= intersectx1 and intersecty0 <= intersecty1 and intersectz0 <= intersectz1:
                update[(intersectx0, intersectx1, intersecty0, intersecty1, intersectz0, intersectz1)] -= osign
        if sign > 0:
            update[(x0, x1, y0, y1, z0, z1)] += sign
        cubes.update(update)

    return sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
               for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())


def main():
    data = get_input(22, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()