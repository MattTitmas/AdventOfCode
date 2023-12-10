from collections import Counter
from functools import lru_cache
from itertools import product


def part1():
    positions = [int(i.split(": ")[1]) for i in open("input.txt").read().split("\n")]
    scores = [0, 0]
    turn = 0
    rolls = 0
    currentRoll = 1
    while scores[0] < 1000 and scores[1] < 1000:
        nextRolls = [
            currentRoll,
            100 if (currentRoll + 1) % 100 == 0 else (currentRoll + 1) % 100,
            100 if (currentRoll + 2) % 100 == 0 else (currentRoll + 2) % 100,
        ]
        rolls += 3
        currentRoll = 100 if (currentRoll + 3) % 100 == 0 else (currentRoll + 3) % 100
        positions[turn] = (((positions[turn] + sum(nextRolls)) - 1) % 10) + 1
        scores[turn] += positions[turn]
        turn = (turn + 1) % 2
    return min(scores) * rolls


@lru_cache(maxsize=None)
def part2(player1Position=-1, player2Position=-1, player1Score=0, player2Score=0):
    if player1Position == -1 or player2Position == -1:
        positions = [
            int(i.split(": ")[1]) for i in open("input.txt").read().split("\n")
        ]
        player1Position = positions[0]
        player2Position = positions[1]
    if player1Score >= 21:
        return 1, 0
    if player2Score >= 21:
        return 0, 1
    result = [0, 0]
    for roll, freq in dice_freq.items():
        position = ((player1Position + roll - 1) % 10) + 1
        score = player1Score + position
        player2Wins, player1Wins = part2(player2Position, position, player2Score, score)
        result[0] += freq * player1Wins
        result[1] += freq * player2Wins
    return result


dice_freq = Counter(sum(p) for p in product((1, 2, 3), repeat=3))

print(f"answer to part1: {part1()}")
print(f"answer to part2: {max(part2())}")
