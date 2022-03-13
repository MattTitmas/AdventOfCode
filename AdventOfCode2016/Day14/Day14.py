from hashlib import md5

def part1():
    values = open("input.txt").read()
    values = "abc"
    current = 0
    keys = []
    while len(keys) != 64:
        result = md5((values+str(current)).encode()).hexdigest()
        triple = False
        for i in range(0, len(result)-2):
            if result[i] == result[i+1] and result[i] == result[i+2]:
                triple = True
                letter = result[i]
                break
        if triple:
            for i in range(current+1, current+1001):
                result = md5((values + str(i)).encode()).hexdigest()
                quintuple = False
                for j in range(0, len(result) - 4):
                    if result[j] == letter and result[j] == result[j + 1] and result[j] == result[j + 2] and result[j] == result[j + 3] and result[j] == result[j + 4]:
                        quintuple = True
                        break
                if quintuple:
                    keys.append(current)
                    break
        current += 1
    return keys[-1]


def part2():
    values = open("input.txt").read()
    current = 1001
    oldLength = 0
    keys = []
    md5Hashes = []
    for key in range(0,1001):
        result = values+str(key)
        for i in range(2017):
            result = md5(result.encode()).hexdigest()
        md5Hashes.append(result)

    while len(keys) != 64:
        currentMD5 = md5Hashes.pop(0)
        triple = False
        for i in range(0, len(currentMD5)-2):
            if currentMD5[i] == currentMD5[i+1] and currentMD5[i] == currentMD5[i+2]:
                triple = True
                letter = currentMD5[i]
                break
        if triple:
            for i in range(len(md5Hashes)):
                result = md5Hashes[i]
                quintuple = False
                for j in range(0, len(result) - 4):
                    if result[j] == letter and result[j] == result[j + 1] and result[j] == result[j + 2] and result[j] == result[j + 3] and result[j] == result[j + 4]:
                        quintuple = True
                        break
                if quintuple:
                    keys.append(current-1001)
                    break
        result = values+str(current)
        for i in range(2017):
            result = md5(result.encode()).hexdigest()
        md5Hashes.append(result)
        current += 1
    return keys[-1]



print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")