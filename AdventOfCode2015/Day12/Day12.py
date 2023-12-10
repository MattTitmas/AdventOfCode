from json import loads


def part1():
    value = loads(open("input.txt", "r").read())

    def findNos(data):
        if type(data) == type(dict()):
            return sum(map(findNos, data.values()))
        if type(data) == type(list()):
            return sum(map(findNos, data))
        if type(data) == int:
            return data
        return 0

    return findNos(value)


def part2():
    value = loads(open("input.txt", "r").read())

    def findNos(data):
        if type(data) == type(dict()):
            if "red" in data.values():
                return 0
            return sum(map(findNos, data.values()))
        if type(data) == type(list()):
            return sum(map(findNos, data))
        if type(data) == int:
            return data
        return 0

    return findNos(value)


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
