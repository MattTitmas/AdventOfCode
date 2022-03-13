from base import BaseDay


class Day6(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        with open(self.input_path) as file:
            memory = [int(i) for i in file.read().split("\t")]
        seen_states = set()
        while tuple(memory) not in seen_states:
            seen_states.add(tuple(memory))
            index = memory.index(max(memory))
            value = memory[index]
            memory[index] = 0
            for i in range(value):
                index += 1
                index = index % len(memory)
                memory[index] += 1
        return len(seen_states)


    @property
    def part2(self):
        wanted = [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]
        with open(self.input_path) as file:
            memory = [int(i) for i in file.read().split("\t")]
        seen_states = set()
        seen_before = False
        since = 0
        while tuple(memory) not in seen_states:
            if seen_before:
                since += 1
            seen_states.add(tuple(memory))
            index = memory.index(max(memory))
            value = memory[index]
            memory[index] = 0
            for i in range(value):
                index += 1
                index = index % len(memory)
                memory[index] += 1
            if memory == wanted:
                if seen_before:
                    return since
                else:
                    seen_before = True

