from utils import get_input
import numpy as np

def part1(data):
    n = max([max(line) for line in lines])
    ocean = np.zeros((n+1,n+1))
    for line in lines:
        if line[0]==line[2]:
            if line[3]>line[1]:
                for i in range(line[1], line[3]+1):
                    ocean[line[0],i] += 1
            else:
                for i in range(line[3], line[1]+1):
                    ocean[line[0],i] += 1
        if line[1]==line[3]:
            if line[2]>line[0]:
                for i in range(line[0], line[2]+1):
                    ocean[i,line[1]] += 1
            else:
                for i in range(line[2], line[0]+1):
                    ocean[i,line[1]] += 1
    return np.sum(ocean>1)

def part2(data):
    n = max([max(line) for line in lines])
    ocean = np.zeros((n+1,n+1))
    for line in lines:
        if line[0]==line[2]:
            if line[3]>line[1]:
                for i in range(line[1], line[3]+1):
                    ocean[line[0],i] += 1
            else:
                for i in range(line[3], line[1]+1):
                    ocean[line[0],i] += 1
        if line[1]==line[3]:
            if line[2]>line[0]:
                for i in range(line[0], line[2]+1):
                    ocean[i,line[1]] += 1
            else:
                for i in range(line[2], line[0]+1):
                    ocean[i,line[1]] += 1
        if abs(line[0]-line[2])==abs(line[1]-line[3]):
            diff_x = line[0]-line[2]
            diff_y = line[1]-line[3]
            if diff_x < 0:
                for i in range(line[0],line[2]+1):
                    if diff_y < 0:
                        ocean[i,line[1]+i-line[0]] += 1
                    else:
                        ocean[i,line[1]-i+line[0]] += 1
            else:
                for i in range(line[2],line[0]+1):
                    if diff_y < 0:
                        ocean[i,line[1]-i+line[0]] += 1
                    else:
                        ocean[i,line[3]+i-line[2]] += 1
    return np.sum(ocean>1)

def get_lines(data):
    lines = []
    for line in data:
        start, end = line.split('->')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        lines.append((int(start_x), int(start_y), int(end_x), int(end_y)))
    return lines


if __name__ == "__main__":
    day = 5
    data = get_input(day)
    lines = get_lines(data)
    print(part1(lines))
    print(part2(lines))

