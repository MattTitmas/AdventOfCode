from aoc import get_input
from utils import function_timer, function_timer_avg


@function_timer_avg
def part1(data):
    tree_heights = [list(map(int, list(i))) for i in data.split('\n')]
    possible = set()
    for i in range(len(tree_heights)):
        max_so_far_i_j = -1
        max_so_far_j_i = -1
        for j in range(len(tree_heights[i])):
            if tree_heights[i][j] > max_so_far_i_j:
                max_so_far_i_j = tree_heights[i][j]
                possible.add((i, j))
            if tree_heights[j][i] > max_so_far_j_i:
                max_so_far_j_i = tree_heights[j][i]
                possible.add((j, i))

    for i in range(len(tree_heights)):
        max_so_far_i_j = -1
        max_so_far_j_i = -1
        for j in range(len(tree_heights[i])-1, -1, -1):
            if tree_heights[i][j] > max_so_far_i_j:
                max_so_far_i_j = tree_heights[i][j]
                possible.add((i, j))
            if tree_heights[j][i] > max_so_far_j_i:
                max_so_far_j_i = tree_heights[j][i]
                possible.add((j, i))

    return len(possible)


@function_timer_avg
def part2(data):
    tree_heights = [list(map(int, list(i))) for i in data.split('\n')]
    max_score = 0
    for i in range(len(tree_heights)):
        for j in range(len(tree_heights[i])):
            # left
            left = 0
            for k in range(j-1, -1, -1):
                left += 1
                if tree_heights[i][k] >= tree_heights[i][j]:
                    break
            # right
            right = 0
            for k in range(j + 1, len(tree_heights[i])):
                right += 1
                if tree_heights[i][k] >= tree_heights[i][j]:
                    break

            # up
            up = 0
            for k in range(i-1, -1, -1):
                up += 1
                if tree_heights[k][j] >= tree_heights[i][j]:
                    break

            # down
            down = 0
            for k in range(i + 1, len(tree_heights[i])):
                down += 1
                if tree_heights[k][j] >= tree_heights[i][j]:
                    break
            max_score = max(max_score, up*left*down*right)
    return max_score



def main():
    data = get_input(8, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
