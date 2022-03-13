def isNice1(s: str) -> bool:
    if ("ab" in s or "cd" in s or "pq" in s or "xy" in s):
        return False
    if sum([s.lower().count(x) for x in "aeiou"]) < 3:
        return False
    for x in range(0, len(s)-1):
        if s[x] == s[x+1]:
            return True
    return False

def isNice2(s: str) -> bool:
    toRet = False
    for x in range(0, len(s)-2):
        currentString = s[x]+s[x+1]
        newString = s[0:x:] + "-" + s[x+2::]
        if currentString in newString:
            toRet = True
            break
    for x in range(0, len(s)-2):
        if s[x] == s[x+2]:
            return toRet
    return False


def part1():
    values = open("input.txt","r").read().split("\n")
    return sum([isNice1(string) for string in values])
    
        

def part2():
    values = open("input.txt","r").read().split("\n")
    return sum([isNice2(string) for string in values])

print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
    
