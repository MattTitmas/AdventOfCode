import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def part1():
    wanted = int(open("input.txt", "r").read())
    current = 700000
    while current > 0:
        current += 1
        total = int(10 * sum(list(divisorGenerator(current))))
        if total > wanted:
            return current


def part2():
    wanted = int(open("input.txt", "r").read())
    current = 700000
    while current > 0:
        current += 1
        total = int(
            11 * sum(i for i in list(divisorGenerator(current)) if current <= i * 50)
        )
        if total > wanted:
            return current


print(f"answer to part1: {part1()}")
print(f"answer to part2: {part2()}")
