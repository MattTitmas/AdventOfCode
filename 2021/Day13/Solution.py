from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    points = [[int(j) for j in i.split(",")] for i in data.split("\n\n")[0].split("\n")]
    folds = [[int(j) if j.isnumeric() else j for j in i.split("along ")[1].split("=")] for i in data.split("\n\n")[1].split("\n")]

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

@function_timer_avg
def part2(data):
    points = [[int(j) for j in i.split(",")] for i in data.split("\n\n")[0].split("\n")]
    folds = [[int(j) if j.isnumeric() else j for j in i.split("along ")[1].split("=")] for i in data.split("\n\n")[1].split("\n")]

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


def main():
    data = get_input(13, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()

