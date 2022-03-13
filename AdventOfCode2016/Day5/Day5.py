from hashlib import md5

def part1():
    values = open("input.txt").read()
    current = 0
    code = ""
    while len(code) != 8:
        result = md5((values+str(current)).encode()).hexdigest()
        if result[0:5] == "00000":
            code += result[5]
        current += 1
    return code


def part2():
    values = open("input.txt").read()
    current = 0
    code = "________"
    while "_" in code:
        result = md5((values+str(current)).encode()).hexdigest()
        if result[0:5] == "00000":
            position = result[5]
            if position.isnumeric() and int(position) < 8 and code[int(position)] == "_":
                code = code[:int(position)] + result[6] + code[int(position) + 1:]
        current += 1
    return code


print(f"Answer to part 1: {part1()}")
print(f"Answer to part 2: {part2()}")