from utils import *
import numpy as np

def part1(data):
    """
    Super naive :)
    """
    cube_map = np.array([[[0 for z in range(101)] for y in range(101)] for x in range(101)])
    for mode, coordinates in data:
        if mode == "on": val = 1
        else: val = 0
        x_range, y_range, z_range = coordinates
        if not (-50 <= x_range[0] <= x_range[1] <= 50) or \
        not (-50 <= y_range[0] <= y_range[1] <= 50) or \
        not (-50 <= z_range[0] <= z_range[1] <= 50):   
            continue    
        cube_map[x_range[0]+50:x_range[1]+51, y_range[0]+50:y_range[1]+51, z_range[0]+50:z_range[1]+51] = val
    return np.sum(cube_map)

def part2(data):
    """
    slow (~10s) but works! :) 
    """
    cuboids = []
    for mode, coordinates in data:
        cuboids_to_add = [(mode,coordinates)]
        while cuboids_to_add:
            cuboid_to_add = cuboids_to_add.pop(0)
            overlaps = False
            for i in range(len(cuboids)):
                cuboid = cuboids[i]
                if overlap(cuboid[1], cuboid_to_add[1]):
                    overlaps = True
                    del cuboids[i]
                    # non-overlapping subcuboids
                    cuboids_to_add += subcuboids(cuboid, cuboid_to_add)
                    break
            if not overlaps:
                cuboids.append(cuboid_to_add)

    s = 0
    #print("\n final cuboids")
    for c in cuboids:
        #print(c, volume(c[1]))
        if c[0] == 'on':
            s += volume(c[1])
    return s

def volume(cuboid):
    x, y, z = cuboid
    return (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])

def overlap(coord_a, coord_b):
    x_a, y_a, z_a = coord_a
    x_b, y_b, z_b = coord_b
    if x_a[1] > x_b[0] and x_b[1] > x_a[0]: #overlap x-coord
        if y_a[1] > y_b[0] and y_b[1] > y_a[0]: #overlap y-coord
            if z_a[1] > z_b[0] and z_b[1] > z_a[0]: #overlap z-coord
                return True
    return False

def subcuboids(cuboid_a, cuboid_b):
    #print('a', cuboid_a)
    #print('b', cuboid_b)
    new_cuboids = []
    x_a, y_a, z_a = cuboid_a[1]
    x_b, y_b, z_b = cuboid_b[1]
    if x_a[0] < x_b[0]:
        #print("case 0",x_a,x_b)
        #print("append",[x_a[0], x_b[0]])
        new_cuboids.append((cuboid_a[0], ([x_a[0], x_b[0]],y_a.copy(),z_a.copy())))
        x_a[0] = x_b[0]
    if x_a[1] > x_b[1]:
        #print("case 1",x_a,x_b)
        #print("append",[x_b[1], x_a[1]])
        new_cuboids.append((cuboid_a[0], ([x_b[1], x_a[1]],y_a.copy(),z_a.copy())))
        x_a[1] = x_b[1]
    if y_a[0] < y_b[0]:
        #print("case 2",y_a,y_b)
        #print("append",[y_a[0], y_b[0]])
        new_cuboids.append((cuboid_a[0], (x_a.copy(),[y_a[0], y_b[0]],z_a.copy())))
        y_a[0] = y_b[0]
    if y_a[1] > y_b[1]:
        #print("case 3",y_a,y_b)
        #print("append",[y_b[1], y_a[1]])
        new_cuboids.append((cuboid_a[0], (x_a.copy(),[y_b[1], y_a[1]],z_a.copy())))
        y_a[1] = y_b[1]
    if z_a[0] < z_b[0]:
        #print("case 4",z_a,z_b)
        #print("append",[z_a[0], z_b[0]])
        new_cuboids.append((cuboid_a[0], (x_a.copy(),y_a.copy(),[z_a[0], z_b[0]])))
        z_a[0] = z_b[0]
    if z_a[1] > z_b[1]:
        #print("case 5",z_a,z_b)
        #print("append",[z_b[1], z_a[1]])
        new_cuboids.append((cuboid_a[0], (x_a.copy(),y_a.copy(),[z_b[1], z_a[1]])))
        z_a[1] = z_b[1]
    new_cuboids.append(cuboid_b)
    #print(new_cuboids)
    return new_cuboids


def process_input(data, p2=False):
    reboot_steps = []
    for line in data:
        mode, coord = line.split()
        coord = coord.replace('x=','').replace(',y','').replace(',z','')
        coord = [[int(y) for y in x.split('..')] for x in coord.split('=')]
        if p2:
            coord[0][1] += 1
            coord[1][1] += 1
            coord[2][1] += 1
        reboot_steps.append((mode, coord))
    return reboot_steps

if __name__ == "__main__":
    day = 22
    data = get_input(day)
    #data = get_file("example22.txt")
    #data="""on x=0..1,y=1..2,z=0..0
#on x=1..2,y=1..2,z=0..0
#off x=1..1,y=1..1,z=0..0""".splitlines()
    print(part1(process_input(data)))
    print(part2(process_input(data, p2=True)))
