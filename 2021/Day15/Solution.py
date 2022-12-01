def part1():
    values = [[int(j) for j in list(i)] for i in open("input.txt").read().split("\n")]

    risk = [[float("inf") for i in range(len(values[0]))] for j in range(len(values))]
    risk[0][0] = 0

    change = True
    while change:
        change = False
        for i in range(0,len(values)):
            for j in range(0,len(values[i])):
                current = (i,j)
                for x in range(max(0,current[0]-1),min(100,current[0]+2)):
                    for y in range(max(0,current[1]-1),min(100,current[1]+2)):
                        if (abs(current[0]-x) != abs(current[1]-y)):
                            value = risk[x][y] + values[i][j]
                            if value < risk[i][j]:
                                risk[i][j] = value
                                change = True
    return risk[-1][-1]


def part2():
    values = [[int(j) for j in list(i)] for i in open("input.txt").read().split("\n")]

    for x in range(4):
        for i in range(0,len(values)):
            lst = values[i][x*100:(x+1)*100]
            values[i] = values[i] + [j+1 if (j+1) < 10 else (j+1)-9 for j in lst]

    for y in range(4):
        for i in range(y*100,(y+1)*100):
            values.append([j+1 if (j+1) < 10 else (j+1)-9 for j in values[i]])

    
    risk = [[float("inf") for i in range(len(values[0]))] for j in range(len(values))]
    risk[0][0] = 0

    change = True
    while change:
        change = False
        for i in range(0,len(values)):
            for j in range(0,len(values[i])):
                current = (i,j)
                for x in range(max(0,current[0]-1),min(100*5,current[0]+2)):
                    for y in range(max(0,current[1]-1),min(100*5,current[1]+2)):
                        if (abs(current[0]-x) != abs(current[1]-y)):
                            value = risk[x][y] + values[i][j]
                            if value < risk[i][j]:
                                risk[i][j] = value
                                change = True
    return risk[-1][-1]
print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
    
