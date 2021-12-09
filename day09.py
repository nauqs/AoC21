from utils import get_input
import numpy as np

def part1(data):
    data = np.pad(data, 1, mode='maximum')
    mask_r = data-np.roll(data,shift=1,axis=-1)<0
    mask_l = data-np.roll(data,shift=-1,axis=-1)<0
    mask_u = data-np.roll(data,shift=1,axis=0)<0
    mask_d = data-np.roll(data,shift=-1,axis=0)<0
    low_points = data[(mask_r & mask_l & mask_u & mask_d)]+1
    return np.sum(low_points)

def part2(data):
    data = np.pad(data, 1, mode='maximum')
    mask_r = data-np.roll(data,shift=1,axis=-1)<0
    mask_l = data-np.roll(data,shift=-1,axis=-1)<0
    mask_u = data-np.roll(data,shift=1,axis=0)<0
    mask_d = data-np.roll(data,shift=-1,axis=0)<0
    low_points = []
    low_points_indices = np.where(mask_r & mask_l & mask_u & mask_d)
    for idx, idy in zip(low_points_indices[0],low_points_indices[1]):
        low_points.append((idx, idy))

    sizes = []
    for point in low_points:
        sizes.append(get_basin_size(data, point))
    return np.prod(sorted(sizes)[-3:])

def get_basin_size(data, point):
    basin = [point]
    stack_points = [point]
    current_point = point
    while stack_points:
        current_point = stack_points.pop()
        new_points, basin = get_adjacent_basin(data, basin, current_point)
        stack_points = stack_points + new_points
    return len(basin)

def get_adjacent_basin(data, basin, point):
    adj_basin = [point]
    if data[point[0],point[1]-1]!=9:
        adj_basin.append((point[0],point[1]-1))
    if data[point[0],point[1]+1]!=9:
        adj_basin.append((point[0],point[1]+1))
    if data[point[0]+1,point[1]]!=9:
        adj_basin.append((point[0]+1,point[1]))
    if data[point[0]-1,point[1]]!=9:
        adj_basin.append((point[0]-1,point[1]))

    new_points = []
    for p in adj_basin:
        if p not in basin:
            new_points.append(p)
            basin.append(p)

    return new_points, basin

if __name__ == "__main__":
    day = 9
    data = np.array([[int(x) for x in line] for line in get_input(day)])
    print(part1(data))
    print(part2(data))

