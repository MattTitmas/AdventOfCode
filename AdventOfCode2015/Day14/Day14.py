def part1():
    reindeers = {i.split(" can")[0]:[int(j) for j in [i.split(" ")[3], i.split(" ")[6], i.split(" ")[-2]]] for i in open("input.txt","r").read().split("\n")}
    seconds = 2503
    maxDist = 0
    for reindeer, speed in reindeers.items():
        totalTime = speed[1]+speed[2]
        distanceTravelled = speed[0] * speed[1] * int(seconds/totalTime)
        timeSpentFlying = totalTime * int(seconds/totalTime)
        distanceTravelled += speed[0] * min(speed[1], seconds-timeSpentFlying)
        maxDist = max(maxDist, distanceTravelled)
    return maxDist

def part2():
    reindeers = {i.split(" can")[0]:[int(j) for j in [i.split(" ")[3], i.split(" ")[6], i.split(" ")[-2]]] for i in open("input.txt","r").read().split("\n")}
    points = {i.split(" can")[0] : 0 for i in open("input.txt","r").read().split("\n")}
    distance = {i.split(" can")[0]: 0 for i in open("input.txt", "r").read().split("\n")}
    for second in range(0, 2503):
        for reindeer, speed in reindeers.items():
            time = (speed[1]+speed[2])*int(second / (speed[1]+speed[2]))
            distance[reindeer] += speed[0] if (second - time < speed[1]) else 0
        maxDist = max(distance.values())
        for key in distance.keys():
            if distance[key] == maxDist:
                points[key] += 1
    return max(points.values())

print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")

