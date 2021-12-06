from utils import get_input
from collections import defaultdict

def simulate(data, days):
    fishes = defaultdict(int)
    for fish in data.split(','):
        fishes[int(fish)] += 1

    for day in range(days):
        new_fishes = defaultdict(int)
        for timer in range(9):
            if timer != 0:
                new_fishes[timer-1] += fishes[timer]
            else:
                new_fishes[6] += fishes[0]
                new_fishes[8] = fishes[0]
        fishes = new_fishes.copy()
    return sum(fishes.values())



if __name__ == "__main__":
    day = 6
    data = get_input(day, splitlines=False)
    print(simulate(data, 80))
    print(simulate(data, 256))