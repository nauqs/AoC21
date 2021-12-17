from utils import get_input
import numpy as np

def part1(x_min, x_max, y_min, y_max):
    """
    brute force 1 :)
    """
    h_max = 0
    for x_vel in range(x_max+1):
        for y_vel in range(2*abs(y_max)):
            res = shoot(x_vel, y_vel, x_min, x_max, y_min, y_max)
            if res:
                h_max = max(h_max, res)    
    return h_max

def part2(x_min, x_max, y_min, y_max):
    """
    brute force 2 :)
    """
    s = 0
    for x_vel in range(x_max+1):
        for y_vel in range(y_min,2*abs(y_max)):
            res = shoot(x_vel, y_vel, x_min, x_max, y_min, y_max)
            if res:
                s+=1    
    return s

def shoot(x_vel, y_vel, x_min, x_max, y_min, y_max):
    x_pos, y_pos = 0, 0
    h_max = 1
    target = False
    while (x_pos < x_max and y_pos > y_min) and not target:
        x_pos += x_vel
        y_pos += y_vel
        x_vel -= np.sign(x_vel)
        y_vel -= 1
        target = x_min <= x_pos <= x_max and y_min <= y_pos <= y_max
        h_max = max(h_max, y_pos)
    if target:
        return h_max
    else:
        return False

if __name__ == "__main__":
    day = 17
    data = [x.split("=")[1] for x in get_input(day, splitlines=False).split(',')]
    x_min, x_max = data[0].split('..')
    y_min, y_max = data[1].split('..')
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    print(part1(x_min, x_max, y_min, y_max))
    print(part2(x_min, x_max, y_min, y_max))

