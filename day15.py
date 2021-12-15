from utils import get_input
import numpy as np

def part1(data):
    """
    branch&bound: very slow for part 2 (~30s) :(
    """
    n = len(data)
    stack = [([(0,0)], 0)]
    min_path, min_risk = get_greedy_path(data)
    print("greedy:",min_risk)

    min_risk_map = np.zeros((n, n))+min_risk

    while stack:
        stack.sort(key=lambda x: -x[1])
        c_path, c_risk = stack.pop()
        x, y = c_path[-1]
        for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
            nx, ny = x+dx, y+dy
            if nx == n-1 and ny == n-1:
                new_risk = c_risk + data[nx][ny]
                if new_risk < min_risk:
                    min_risk = c_risk+data[-1][-1]
                    min_path = c_path.copy()
                    min_path.append((nx,ny))

            elif 0 <= nx < n and 0 <= ny < n:
                new_risk = c_risk + data[nx][ny]
                if (nx,ny) not in c_path and new_risk<min_risk:
                    if new_risk < min_risk_map[nx,ny]:
                        min_risk_map[nx,ny] = new_risk
                        stack.append((c_path+[(nx,ny)], new_risk))

    return int(min_risk)

def get_greedy_path(data):
    x, y = 0, 0
    path = [(0,0)]
    s = 0
    while x != len(data)-1 or y != len(data[0]) -1:
        if x != len(data)-1 and y != len(data[0])-1:
            if data[x+1][y] > data[x][y+1]:
                y += 1
            else:
                x += 1
        elif x == len(data)-1:
            y += 1
        elif y == len(data)-1:
            x += 1
        path.append((x,y))
        s += data[x][y]   
    return path, int(s)

def get_full_map(data):
    n = len(data)
    new_map = np.zeros((5*n,5*n))
    for i in range(5*n):
        for j in range(5*n):
            ki = i // n 
            kj = j // n
            new_map[i,j] = (ki + kj + data[i%n, j%n] - 1) % 9 + 1
    return new_map

def part2(data):
    return part1(get_full_map(data))


if __name__ == "__main__":
    day = 15
    data = np.array([[int(x) for x in line] for line in get_input(day)])
    print(part1(data))
    print(part2(data))
