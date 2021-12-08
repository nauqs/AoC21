from utils import get_input
import numpy as np

def part1(data):
    return np.min([np.sum(np.abs(data-x)) for x in range(data.min(), data.max())])

def part2(data):
    return np.min([np.sum([get_cost(y) for y in np.abs(data-x)]) for x in range(data.min(), data.max())])

def get_cost(n):
    return n*(n+1)/2

if __name__ == "__main__":
    day = 7
    data = get_input(day, splitlines=False).split(',')
    data = np.array([int(x) for x in data])
    print(int(part1(data)))
    print(int(part2(data)))

