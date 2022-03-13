from base import BaseDay


class Day1(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        with open(self.input_path) as file:
            numbers = [int(i) for i in list(file.read())]
        total = 0
        for i, value in enumerate(numbers):
            if value == numbers[(i+1) % len(numbers)]:
                total += value
        return total

    @property
    def part2(self):
        with open(self.input_path) as file:
            numbers = [int(i) for i in list(file.read())]
        jump = int(len(numbers)/2)
        total = 0
        for i, value in enumerate(numbers):
            if value == numbers[(i+jump) % len(numbers)]:
                total += value
        return total