from base import BaseDay


class Day2(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        with open(self.input_path) as file:
            spreadsheet = [[int(j) for j in i.split("\t")] for i in file.read().split("\n")]
        total = 0
        for line in spreadsheet:
            total += max(line) - min(line)
        return total

    @property
    def part2(self):
        with open(self.input_path) as file:
            spreadsheet = [[int(j) for j in i.split("\t")] for i in file.read().split("\n")]
        total = 0
        for line in spreadsheet:
            for i, val1 in enumerate(line):
                for j, val2 in enumerate(line):
                    if i != j and val1 % val2 == 0:
                        total += int(val1 / val2)
        return total