from itertools import permutations


def snailfishAdd(num1: list, num2: list) -> list:
    result = ["["] + num1 + num2 + ["]"]
    changeMade = True
    while changeMade:
        changeAlreadyMade = False
        nestedLevel = 0
        for i in range(len(result)):
            char = result[i]
            if char == "[":
                nestedLevel += 1
            elif char == "]":
                nestedLevel -= 1
            if char.isnumeric() and nestedLevel >= 5:
                for b in range(i - 1, -1, -1):
                    if result[b].isnumeric():
                        result[b] = str(int(result[b]) + int(result[i]))
                        break
                for f in range(i + 2, len(result)):
                    if result[f].isnumeric():
                        result[f] = str(int(result[f]) + int(result[i + 1]))
                        break
                for j in range(i + 2, i - 2, -1):
                    result.pop(j)
                result.insert(i - 1, "0")
                changeAlreadyMade = True
                break
        if not changeAlreadyMade:
            for i in range(len(result)):
                char = result[i]
                if char.isnumeric() and int(char) > 9:
                    val1 = int(char) // 2
                    val2 = int(char) // 2 + int(char) % 2
                    result.pop(i)
                    result.insert(i, "]")
                    result.insert(i, str(val2))
                    result.insert(i, str(val1))
                    result.insert(i, "[")
                    changeAlreadyMade = True
                    break
        changeMade = False
        if changeAlreadyMade:
            changeMade = True
    return result


def getMag(num: str) -> int:
    left, right = "", ""
    nestedLevel = 0
    for i in range(2, len(num) - 1, 2):
        char = num[i]
        if char == "[":
            nestedLevel += 1
        elif char == "]":
            nestedLevel -= 1
        if nestedLevel == 0:
            left = num[2 : i + 1]
            right = num[i + 2 : len(num) - 2]
            break
    left = int(left[0]) if len(left) == 1 else getMag(left)
    right = int(right[-1]) if len(right) == 1 else getMag(right)
    return 3 * left + 2 * right


def part1():
    values = [list(i) for i in open("input.txt").read().split("\n")]
    for i in range(len(values)):
        values[i] = list(filter(lambda a: a != ",", values[i]))
    result = values[0]
    for i in range(1, len(values)):
        result = snailfishAdd(result, values[i])
    return getMag(" ".join(result))


def part2():
    values = [list(i) for i in open("input.txt").read().split("\n")]
    for i in range(len(values)):
        values[i] = list(filter(lambda a: a != ",", values[i]))
    maxMag = -float("inf")
    count = 0
    for i in permutations(values, 2):
        count += 1
        result = snailfishAdd(i[0], i[1])
        maxMag = max(maxMag, getMag(" ".join(result)))
    return maxMag


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
