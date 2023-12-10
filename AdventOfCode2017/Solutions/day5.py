from base import BaseDay


class Day5(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        with open(self.input_path) as file:
            jumps = [int(i) for i in file.read().split("\n")]

        currentPos = 0
        count = 0
        while True:
            newPos = currentPos + jumps[currentPos]
            jumps[currentPos] += 1
            currentPos = newPos
            count += 1
            if currentPos < 0 or currentPos >= len(jumps):
                return count

    @property
    def part2(self):
        with open(self.input_path) as file:
            jumps = [int(i) for i in file.read().split("\n")]

        currentPos = 0
        count = 0
        while True:
            try:
                newPos = currentPos + jumps[currentPos]
            except IndexError:
                return count
            jumps[currentPos] = (
                jumps[currentPos] - 1
                if jumps[currentPos] >= 3
                else jumps[currentPos] + 1
            )
            currentPos = newPos
            count += 1
