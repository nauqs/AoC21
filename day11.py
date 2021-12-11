from utils import get_input
import numpy as np

def part1(data):
    return count_flashes(data.copy(), 100)

def part2(data):
    return count_flashes(data.copy(), 9999)

def count_flashes(data, steps):
    f = 0
    for step in range(steps):
        flashed = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
        while np.max(data)>9:
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j]>9 and (i,j) not in flashed:
                        data[i][j] = 0
                        f += 1
                        flashed.append((i,j))
                        for di, dj in [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]:
                            if 0 <= i+di < len(data):
                                if 0 <= j+dj < len(data[i+di]):
                                    if (i+di,j+dj) not in flashed:
                                        data[i+di][j+dj] += 1
        if len(flashed)==len(data)*len(data[0]): #reuse code for part 2
            return(step+1)
    return f

if __name__ == "__main__":
    day = 11
    data = np.array([[int(x) for x in line] for line in get_input(day)])
    print(part1(data))
    print(part2(data))

