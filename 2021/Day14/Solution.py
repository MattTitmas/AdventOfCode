from aoc import get_input
from utils import function_timer_avg, function_timer


@function_timer_avg
def part1(data):
    code = data.split("\n\n")[0]
    keys = {i.split(" -> ")[0]:i.split(" -> ")[1] for i in data.split("\n\n")[1].split("\n")}
    string = {}

    for i in range(0,len(code)-1):
        string[code[i]+code[i+1]] = 1 if code[i]+code[i+1] not in string else string[code[i]+code[i+1]]+1

    for i in range(11):
        copy = dict(string)
        for key,value in copy.items():
            if (value > 0 and key in keys):
                string[key[0]+keys[key]] = value if key[0]+keys[key] not in string else string[key[0]+keys[key]] + value
                string[keys[key]+key[1]] = value if keys[key]+key[1] not in string else string[keys[key]+key[1]] + value
                string[key] -= value

    occurences = {}
    for key, value in copy.items():
        occurences[key[0]] = value if key[0] not in occurences else occurences[key[0]]+value
        occurences[key[1]] = value if key[1] not in occurences else occurences[key[1]]+value
    occurences[code[0]] += 1
    occurences[code[-1]] += 1
    for key in occurences.keys():
        occurences[key] //= 2
    return(max(occurences.values()) - min(occurences.values()))

@function_timer_avg
def part2(data):
    code = data.split("\n\n")[0]
    keys = {i.split(" -> ")[0]:i.split(" -> ")[1] for i in data.split("\n\n")[1].split("\n")}
    string = {}

    for i in range(0,len(code)-1):
        string[code[i]+code[i+1]] = 1 if code[i]+code[i+1] not in string else string[code[i]+code[i+1]]+1

    for i in range(41):
        copy = dict(string)
        for key,value in copy.items():
            if (value > 0 and key in keys):
                string[key[0]+keys[key]] = value if key[0]+keys[key] not in string else string[key[0]+keys[key]] + value
                string[keys[key]+key[1]] = value if keys[key]+key[1] not in string else string[keys[key]+key[1]] + value
                string[key] -= value

    occurences = {}
    for key, value in copy.items():
        occurences[key[0]] = value if key[0] not in occurences else occurences[key[0]]+value
        occurences[key[1]] = value if key[1] not in occurences else occurences[key[1]]+value
    occurences[code[0]] += 1
    occurences[code[-1]] += 1
    for key in occurences.keys():
        occurences[key] //= 2
    return(max(occurences.values()) - min(occurences.values()))
def main():
    data = get_input(14, 2021)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
    
