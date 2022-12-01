def part1():
    points = [[int(j) for j in i.split(",")] for i in open("input.txt","r").read().split("\n\n")[0].split("\n")]
    folds = [[int(j) if j.isnumeric() else j for j in i.split("along ")[1].split("=")] for i in open("input.txt","r").read().split("\n\n")[1].split("\n")]

    for i in range(0,1):
        direction, amount = folds[i][0],folds[i][1]
        for point in points:
            if direction == 'y':
                if point[1] > amount:
                    diff = abs(point[1]-amount)
                    point[1] = amount - diff
            else:
                if point[0] > amount:
                    diff = abs(point[0]-amount)
                    point[0] = amount - diff
    return len([list(tupl) for tupl in {tuple(item) for item in points}])

        

    return 0

def part2():
    points = [[int(j) for j in i.split(",")] for i in open("input.txt","r").read().split("\n\n")[0].split("\n")]
    folds = [[int(j) if j.isnumeric() else j for j in i.split("along ")[1].split("=")] for i in open("input.txt","r").read().split("\n\n")[1].split("\n")]

    for i in range(0,len(folds)):
        direction, amount = folds[i][0],folds[i][1]
        for point in points:
            if direction == 'y':
                if point[1] > amount:
                    diff = abs(point[1]-amount)
                    point[1] = amount - diff
            else:
                if point[0] > amount:
                    diff = abs(point[0]-amount)
                    point[0] = amount - diff

    
    points = [list(tupl) for tupl in {tuple(item) for item in points}]
    greatestX, greatestY = 0, 0
    for point in points:
        greatestX = max(greatestX, point[0])
        greatestY = max(greatestY, point[1])
    for y in range(greatestY+1):
        string = ""
        for x in range(greatestX+1):
            if [x,y] in points:
                string += "#"
            else:
                string += " "
        print(string)

    
    return 0

print(f"answer to part1: {part1()}")
print(f"answer to part2:")
part2()
    
