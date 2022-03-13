from base import BaseDay
from collections import defaultdict

class Day8(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    def check(self, a, command, b):
        if command == "==":
            return a == b
        elif command == "!=":
            return a != b
        elif command == "<":
            return a < b
        elif command == ">":
            return a > b
        elif command == "<=":
            return a <= b
        elif command == ">=":
            return a >= b

    @property
    def part1(self):
        with open(self.input_path) as file:
            commands = [[[int(k) if k.strip("-").isnumeric() else k for k in j.split(" ")] for j in i.split(" if ")] for i in file.read().split("\n")]
        registers = defaultdict(int)
        for i in commands:
            check_value = registers[i[1][0]]
            update = self.check(check_value, i[1][1], i[1][2])
            if update:
                if i[0][1] == "dec":
                    registers[i[0][0]] -= i[0][2]
                else:
                    registers[i[0][0]] += i[0][2]
        return max(registers.values())

    @property
    def part2(self):
        highest_stored = -float("inf")
        with open(self.input_path) as file:
            commands = [[[int(k) if k.strip("-").isnumeric() else k for k in j.split(" ")] for j in i.split(" if ")] for i in file.read().split("\n")]
        registers = defaultdict(int)
        for i in commands:
            check_value = registers[i[1][0]]
            update = self.check(check_value, i[1][1], i[1][2])
            if update:
                if i[0][1] == "dec":
                    registers[i[0][0]] -= i[0][2]
                else:
                    registers[i[0][0]] += i[0][2]
                highest_stored = max(highest_stored, registers[i[0][0]])
        return highest_stored