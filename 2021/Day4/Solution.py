from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    values = [i for i in data.split("\n\n")]
    order = [int(i) for i in values[0].split(",")]
    boards = [[[(int(j), False) for j in i.split(" ") if j != ""] for i in values[c + 1].split("\n")] for c, x in
              enumerate(values[1:])]
    for key in order:
        for board in boards:
            if any([(key, False) in i for i in board]):

                coords = []
                for x in range(5):
                    for y in range(5):
                        if board[x][y] == (key, False):
                            board[x][y] = (key, True)
                            coords.append((x, y))

                for x, y in coords:
                    if (all([b for (a, b) in board[x]])) or (all([b for (a, b) in ([i[y] for i in board])])):
                        return key * (sum([sum([b for b, c in a if c == False]) for a in board]))


@function_timer_avg
def part2(data):
    values = [i for i in data.split("\n\n")]
    order = [int(i) for i in values[0].split(",")]
    boards = [[[(int(j), False) for j in i.split(" ") if j != ""] for i in values[c + 1].split("\n")] for c, x in
              enumerate(values[1:])]

    for key in order:
        for board in boards[:]:
            if any([(key, False) in i for i in board]):

                coords = []
                for x in range(5):
                    for y in range(5):
                        if board[x][y] == (key, False):
                            board[x][y] = (key, True)
                            coords.append((x, y))

                for x, y in coords:
                    if (all([b for (a, b) in board[x]])) or (all([b for (a, b) in ([i[y] for i in board])])):
                        if len(boards) == 1:
                            return key * (sum([sum([b for b, c in a if c is False]) for a in board]))
                        else:
                            boards.remove(board)


def main():
    data = get_input(4, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
