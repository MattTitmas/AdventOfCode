def Part1():
    File = open("Input.txt").read().split("\n")

    Maximum = -1

    for Code in File:
        RowCode = Code[:-3]
        ColumnCode = Code[7:]

        Maximum = max(
            Maximum,
            (
                int(RowCode.replace("B", "1").replace("F", "0"), 2) * 8
                + int(ColumnCode.replace("R", "1").replace("L", "0"), 2)
            ),
        )

    return Maximum


def Part2():
    File = open("Input.txt").read().split("\n")

    AllSeats = [x for x in range(0, 929)]
    for Code in File:
        RowCode = Code[:-3]
        ColumnCode = Code[7:]

        AllSeats.remove(
            int(RowCode.replace("B", "1").replace("F", "0"), 2) * 8
            + int(ColumnCode.replace("R", "1").replace("L", "0"), 2)
        )

    return AllSeats[-1]


print(Part1())
print(Part2())
