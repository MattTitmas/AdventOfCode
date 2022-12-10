from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [[int(j) for j in i] for i in data.split("\n")]

    total = 0
    for steps in range(100):
        for i in range(len(values)):
            for j in range(len(values[i])):
                values[i][j] += 1
        checked = []
        changeMade = True
        while changeMade:
            changeMade = False
            copy = [i[:] for i in values]
            for i in range(len(copy)):
                for j in range(len(copy[i])):
                    if copy[i][j] > 9 and (i,j) not in checked:
                        checked.append((i,j))
                        changeMade = True
                        for x in range(max(0,i-1),min(len(copy),i+2)):
                            for y in range(max(0,j-1),min(len(copy[i]),j+2)):
                                if (x != i or y != j):
                                    values[x][y] += 1
    
        for i in range(len(values)):
            for j in range(len(values[i])):
                if (values[i][j] > 9):
                    total += 1
                    values[i][j] = 0

        
    return total

@function_timer_avg
def part2(data):
    values = [[int(j) for j in i] for i in data.split("\n")]

    total = 0
    for steps in range(10000):
        for i in range(len(values)):
            for j in range(len(values[i])):
                values[i][j] += 1
        checked = []
        changeMade = True
        while changeMade:
            changeMade = False
            copy = [i[:] for i in values]
            for i in range(len(copy)):
                for j in range(len(copy[i])):
                    if copy[i][j] > 9 and (i,j) not in checked:
                        checked.append((i,j))
                        changeMade = True
                        for x in range(max(0,i-1),min(len(copy),i+2)):
                            for y in range(max(0,j-1),min(len(copy[i]),j+2)):
                                if (x != i or y != j):
                                    values[x][y] += 1

        totalBefore = total
        for i in range(len(values)):
            for j in range(len(values[i])):
                if (values[i][j] > 9):
                    total += 1
                    values[i][j] = 0
        if total-totalBefore == 100:
            return steps+1

def main():
    data = get_input(11, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
    
