from utils import *
import numpy as np
import copy

neighbors = [(1,1),(1,0), (1,-1), (0,1), (0,0), (0,-1), (-1,1), (-1,0), (-1,-1)]

def part1(algo, image):
    n = 2
    output_image = simulate(algo, image, n)
    return np.sum(output_image)

def part2(algo, image):
    n = 50
    output_image = simulate(algo, image, n)
    return np.sum(output_image)

def process_input(data):
    algo, image = data.replace('.','0').replace('#','1').split('\n\n')
    algo = [int(x) for x in list(algo.replace('\n',''))]
    image = [list(map(int, list(x))) for x in image.split('\n')]
    return algo, image

def simulate(algo, image, n):

    for step in range(n):
        new_image = []

        # all 'infinity' values have the same value at each step
        if algo[0]==0:
            infinity_val = 0
        else:
            if step%2==1: infinity_val = algo[0]
            else: infinity_val = algo[511]

        for i in range(-1,len(image)+1):
            new_image_row = []
            for j in range(-1,len(image)+1):
                neighbor_sum, n = 0, 0
                for di,dj in neighbors: #ordered neighbors!!!
                    if 0<=i+di<len(image) and 0<=j+dj<len(image):
                        neighbor_sum += image[i+di][j+dj]*2**n
                    else:
                        neighbor_sum += infinity_val*2**n
                    n += 1
                new_image_row.append(algo[neighbor_sum])
            new_image.append(new_image_row)

        image = copy.deepcopy(new_image)

    return new_image

if __name__ == "__main__":
    day = 20
    data = get_input(day, splitlines=False)
    #data = get_file('example20.txt', splitlines=False)
    algo, image = process_input(data)
    print(part1(algo, image))
    print(part2(algo, image))
