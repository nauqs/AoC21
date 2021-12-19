from utils import *
import numpy as np
from itertools import permutations
from collections import defaultdict

def get_orientations():
    for perm in permutations((0,1,2)):
        for orient in [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]:
            yield perm, orient

def transform(scanner, perm, orientation):
    return [np.multiply((b[perm[0]], b[perm[1]], b[perm[2]]), orientation) for b in scanner]

def part1(data):

    scanners = {(0,0): ((0,0,0), (0,1,2), (1,1,1))}
    print("\nGetting scanner overlaps...")
    for i, sc in enumerate(data):
        print("    scanner",i)
        for j, sc2 in enumerate(data):
            if i!=j:
                matches = False
                correct_p, correct_o, correct_diff = None, None, None
                for p, o in get_orientations():
                    diffs = defaultdict(int)
                    for b in sc:
                        for b2 in transform(sc2, p, o):
                            diffs[tuple(b-b2)] += 1
                    if max(diffs.values())>=12:
                        correct_diff = max(diffs, key=diffs.get)
                        correct_p, correct_o = p, o
                        matches = True
                        break
                if matches:
                    #print(i, j, correct_diff, correct_p, correct_o)
                    scanners[(i,j)] = (correct_diff, correct_p, correct_o)

    scanners_to_0 = get_scanners_to_0(scanners, len(data))  

    total_beacons = []
    origin = {}
    for i, sc in enumerate(data):
        #print("\n\n scanner",i)
        for beacon in sc:
            #print(beacon)
            diff, p, o = scanners_to_0[i]
            perm_beacon = np.array((beacon[p[0]],beacon[p[1]],beacon[p[2]]))
            transformed_beacon = tuple(np.array(diff) + np.multiply(perm_beacon,o))

            #print(transformed_beacon,"\n")

            if transformed_beacon not in total_beacons:
                total_beacons.append(transformed_beacon)
                origin[transformed_beacon] = i

    total_beacons = sorted(total_beacons, key=lambda x: x[0])
    #for beacon in total_beacons:
        #print(beacon, origin[beacon])
    return len(total_beacons)

def get_scanners_to_0(scanners, n):
    print("\nGetting scanners relative positions to scanner 0...\n")
    scanners_to_0 = {0: ((0,0,0), (0,1,2), (1,1,1))}
    #print(scanners,"\n")

    while(len(scanners_to_0)!=n):
        for pair in scanners:
            if pair[1] not in scanners_to_0:
                #print("\nalready have:",list(scanners_to_0.keys()))
                if pair[0]==0:
                    scanners_to_0[pair[1]] = scanners[pair]
                elif pair[0] in scanners_to_0:
                    diff, p, o = scanners_to_0[pair[0]]
                    #print("we have", pair[0], "with", diff, p, o)
                    diff2, p2, o2 = scanners[pair]
                    #print("and", pair[1], "with", diff2, p2, o2)
                    perm_diff2 = np.array((diff2[p[0]],diff2[p[1]],diff2[p[2]]))
                    transformed_diff2 = np.multiply(perm_diff2, o)
                    #print("diff2 transformed to",transformed_diff2)
                    rel_pos_to_0 = tuple(transformed_diff2+diff)
                    #print("rel pos of scanner", pair[1], "to scanner 0:",rel_pos_to_0)
                    transformed_p2 = np.array((p2[p[0]],p2[p[1]],p2[p[2]]))
                    perm_o2 = (o2[p[0]],o2[p[1]],o2[p[2]])
                    total_o = np.multiply(o,perm_o2)
                    #print("relative perm", transformed_p2, ". relative or", total_o, "\n")
                    scanners_to_0[pair[1]] = (rel_pos_to_0, transformed_p2, total_o)

    #for sc in scanners_to_0:
        #print(sc, scanners_to_0[sc])

    return scanners_to_0


def part2(data):

    scanners = {(0,0): ((0,0,0), (0,1,2), (1,1,1))}
    print("\nGetting scanner overlaps...")
    for i, sc in enumerate(data):
        print("    scanner",i)
        for j, sc2 in enumerate(data):
            if i!=j:
                matches = False
                correct_p, correct_o, correct_diff = None, None, None
                for p, o in get_orientations():
                    diffs = defaultdict(int)
                    for b in sc:
                        for b2 in transform(sc2, p, o):
                            diffs[tuple(b-b2)] += 1
                    if max(diffs.values())>=12:
                        correct_diff = max(diffs, key=diffs.get)
                        correct_p, correct_o = p, o
                        matches = True
                        break
                if matches:
                    #print(i, j, correct_diff, correct_p, correct_o)
                    scanners[(i,j)] = (correct_diff, correct_p, correct_o)

    scanners_to_0 = get_scanners_to_0(scanners, len(data))  

    scanner_positions = []
    for sc in scanners_to_0:
        scanner_positions.append(scanners_to_0[sc][0])

    m = 0
    print(scanner_positions)
    for i, pos_1 in enumerate(scanner_positions):
        for j, pos_2 in enumerate(scanner_positions):
            if i!=j:
                m = max(m, manhattan(pos_1,pos_2))

    return m

def manhattan(pos_1,pos_2):
    return np.sum(np.abs(np.array(pos_1)-np.array(pos_2)))

def process_input(data):
    return [[np.array([int(z) for z in y.split(',')]) for y in x.split('\n')[1:]] for x in data.split('\n\n')]


if __name__ == "__main__":
    day = 19
    data = get_input(day, splitlines=False)
    #data = get_file('input19ex.txt', splitlines=False)
    data = process_input(data)
    print(part1(data))
    print(part2(data))