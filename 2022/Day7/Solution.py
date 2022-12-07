from aoc import get_input
from utils import function_timer, function_timer_avg

def generate_folder_sizes(commands):
    folder_sizes = dict()
    current_path = []

    for line in commands:
        if line.split()[1] in {'cd', 'ls', 'dir'}:
            cmd = line.split()[1]

        if cmd == 'cd':
            new_dir = line.split().pop()
            if new_dir == '..':
                current_path.pop()
            elif new_dir == '/':
                current_path = ['/']
            else:
                current_path.append(new_dir)

        else:
            value, name = line.split()
            if value.isnumeric():
                size = int(value)
                for i in range(1, len(current_path)+1):
                    pathname = '/'.join(current_path[:i])
                    folder_sizes[pathname] = folder_sizes.get(pathname, 0) + size
    return folder_sizes

@function_timer
def part1(data):
    folder_sizes = generate_folder_sizes(data.split('\n'))
    return sum([i for i in folder_sizes.values() if i <= 100_000])


@function_timer
def part2(data):
    total_space = 70_000_000
    needed_space = 30_000_000
    folder_sizes = generate_folder_sizes(data.split('\n'))
    need_to_delete = needed_space - (total_space - folder_sizes['/'])
    min_above = float('inf')
    for size in folder_sizes.values():
        if need_to_delete <= size < min_above:
            min_above = size
    return min_above


def main():
    data = get_input(7, 2022)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
