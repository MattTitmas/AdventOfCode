def returnLetter(order, val):
    codes = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
    orderCopy = order[:]
    for char in val:
        orderCopy = [1 if x == char else x for x in orderCopy]
    orderCopy = [0 if x != 1 else x for x in orderCopy]
    return codes.index(orderCopy)

def part1():
    values = [[[k for k in j.split(" ") if k != ""] for j in i.split("|")] for i in open("input.txt","r").read().split("\n")]
    total = 0
    for segment in values:
        for output in segment[1]:
            length = len(output)
            if length == 2 or length == 4 or length == 3 or length == 7:
                 total += 1
    return total

def part2():
    values = [[[k for k in j.split(" ") if k != ""] for j in i.split("|")] for i in open("input.txt","r").read().split("\n")]
    total = 0

    for segment in values:
        amount = {i:0 for i in "abcdefg"}
        length4 = length2 = length3 = ""
        for i in segment[0]:
            if len(i) == 2:
                length2 = i
            if len(i) == 3:
                length3 = i
            if len(i) == 4:
                length4 = i
            for char in i:
                amount[char] += 1
        order = [""]*7
        order[0] = str(min(set(length3).difference(set(length2))))
        amount.pop(str(min(set(length3).difference(set(length2)))))
        order[1] = [key for key,value in amount.items() if value == 8][0]
        amount.pop([key for key,value in amount.items() if value == 8][0])
        order[2] = [key for key,value in amount.items() if value == 9][0]
        amount.pop([key for key,value in amount.items() if value == 9][0])
        order[3] = [key for key,value in amount.items() if value == 7 and key not in length4][0]
        amount.pop([key for key,value in amount.items() if value == 7 and key not in length4][0])
        order[4] = [key for key,value in amount.items() if value == 4][0]
        amount.pop([key for key,value in amount.items() if value == 4][0])
        order[5] = [key for key,value in amount.items() if value == 6][0]
        amount.pop([key for key,value in amount.items() if value == 6][0])
        order[6] = [key for key,value in amount.items() if value == 7][0]
        amount.pop([key for key,value in amount.items() if value == 7][0])
        String = ""
        for inp in segment[1]:
            String += str(returnLetter(order, inp))
        total += int(String)
    return total
        
print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
    
