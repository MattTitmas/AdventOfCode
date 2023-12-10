from base import BaseDay


class Day3(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        return 475
        # Found with maths of Ulam Spiral

    @property
    def part2(self):
        return 279138
        # Found by looking at https://oeis.org/A141481/b141481.txt, https://oeis.org/A141481
