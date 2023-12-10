def part1():
    orderCopy = order[:]
    boardsCopy = boards[:]
    for key in orderCopy:
        for board in boardsCopy:
            if any([(key, False) in i for i in board]):
                coords = []
                for x in range(5):
                    for y in range(5):
                        if board[x][y] == (key, False):
                            board[x][y] = (key, True)
                            coords.append((x, y))

                for x, y in coords:
                    if (all([b for (a, b) in board[x]])) or (
                        all([b for (a, b) in ([i[y] for i in board])])
                    ):
                        return key * (
                            sum([sum([b for b, c in a if c == False]) for a in board])
                        )


def part2():
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
                    if (all([b for (a, b) in board[x]])) or (
                        all([b for (a, b) in ([i[y] for i in board])])
                    ):
                        if len(boards) == 1:
                            return key * (
                                sum(
                                    [
                                        sum([b for b, c in a if c == False])
                                        for a in board
                                    ]
                                )
                            )
                        else:
                            boards.remove(board)


values = [i for i in open("input.txt", "r").read().split("\n\n")]
order = [int(i) for i in values[0].split(",")]
boards = [
    [
        [(int(j), False) for j in i.split(" ") if j != ""]
        for i in values[c + 1].split("\n")
    ]
    for c, x in enumerate(values[1:])
]
print(f"answer to part1: {part1()}")

values = [i for i in open("input.txt", "r").read().split("\n\n")]
order = [int(i) for i in values[0].split(",")]
boards = [
    [
        [(int(j), False) for j in i.split(" ") if j != ""]
        for i in values[c + 1].split("\n")
    ]
    for c, x in enumerate(values[1:])
]
print(f"answer to part2: {part2()}")
