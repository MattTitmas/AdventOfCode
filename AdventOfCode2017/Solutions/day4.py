from base import BaseDay
from collections import Counter


class Day4(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        with open(self.input_path) as file:
            passcodes = [i.split(" ") for i in file.read().split("\n")]
        total = 0
        for passcode in passcodes:
            count = Counter(passcode)
            if count.most_common(1)[0][1] == 1:
                total += 1
        return total

    @property
    def part2(self):
        with open(self.input_path) as file:
            passcodes = [i.split(" ") for i in file.read().split("\n")]
        total = 0
        for passcode in passcodes:
            anagram = False
            for i, val1 in enumerate(passcode):
                for j, val2 in enumerate(passcode):
                    if i != j and sorted(val1) == sorted(val2):
                        anagram = True
            total += 0 if anagram else 1
        return total
