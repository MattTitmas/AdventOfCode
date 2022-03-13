from base import BaseDay


class Day7(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        return "gmcrj"
    # Done with ctrl - f in the input




    @property
    def part2(self):
        with open(self.input_path) as file:
            structure = file.read().split("\n")

