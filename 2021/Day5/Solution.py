def part1():
    values = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in open("input.txt","r").read().split("\n")]
    points = {}
    for line in values:
        if (line[0][0] == line[1][0] or line[0][1] == line[1][1]):
            x = line[0][0]
            y = line[0][1]
            xChange = -1 if (line[1][0] - line[0][0]) < 0 else (1 if (line[1][0] - line[0][0] > 0) else 0)
            yChange = -1 if (line[1][1] - line[0][1]) < 0 else (1 if (line[1][1] - line[0][1] > 0) else 0)
            points[(x,y)] = 1 if (x,y) not in points else points[(x,y)] + 1 

            while (x != line[1][0] or y != line[1][1]):
                x += xChange
                y += yChange
                points[(x,y)] = 1 if (x,y) not in points else points[(x,y)] + 1

    total = 0
    for key, value in points.items():
        total += (1 if value >= 2 else 0)             
    return total

def part2():
    values = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in open("input.txt","r").read().split("\n")]
    points = {}
    for line in values:
        x = line[0][0]
        y = line[0][1]
        xChange = -1 if (line[1][0] - line[0][0]) < 0 else (1 if (line[1][0] - line[0][0] > 0) else 0)
        yChange = -1 if (line[1][1] - line[0][1]) < 0 else (1 if (line[1][1] - line[0][1] > 0) else 0)
        points[(x,y)] = 1 if (x,y) not in points else points[(x,y)] + 1

        while (x != line[1][0] or y != line[1][1]):
            x += xChange
            y += yChange
            points[(x,y)] = 1 if (x,y) not in points else points[(x,y)] + 1

    total = 0
    for key, value in points.items():
        total += (1 if value >= 2 else 0)           
    return total
print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
