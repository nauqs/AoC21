from utils import get_input
import copy

def part1(data):
    sea_map = [list(line) for line in data]
    steps = 0
    moves = True
    n, m  =len(sea_map), len(sea_map[0])

    while moves:
        moves = False
        steps += 1

        new_sea_map = [['.' for _ in range(m)] for _ in range(n)]

        #East-facing herd
        for i in range(n):
            for j in range(m):
                if sea_map[i][j] == '>':
                    if sea_map[i][((j+1)%m)] == '.':
                        moves = True
                        new_sea_map[i][((j+1)%m)] = '>'
                    else:
                        new_sea_map[i][j] = '>'

        #South-facing herd
        for i in range(n):
            for j in range(m):
                if sea_map[i][j] == 'v':
                    if sea_map[(i+1)%n][j] != 'v' and new_sea_map[(i+1)%n][j] != '>':
                        moves = True
                        new_sea_map[(i+1)%n][j] = 'v'
                    else:
                        new_sea_map[i][j] = 'v'

        sea_map = new_sea_map

    return steps

def part2(data):
    return "Free star!"


if __name__ == "__main__":
    day = 25
    data = get_input(day)
    print(part1(data))
    print(part2(data))

