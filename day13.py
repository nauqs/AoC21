from utils import get_input
import numpy as np

def part1(points, folds):
    points = np.array(points)
    paper = np.zeros((np.max(points[:,0])+1, np.max(points[:,1])+1))
    for x, y in points:
        paper[x, y] = 1
    fold_paper = paper.copy()
    for axis, val in folds:
        fold_paper = fold(fold_paper, axis, int(val))
        break
    return int(np.sum(fold_paper))

def part2(points, folds):
    points = np.array(points)
    paper = np.zeros((np.max(points[:,0])+1, np.max(points[:,1])+1))
    for x, y in points:
        paper[x, y] = 1
    fold_paper = paper.copy()
    for axis, val in folds:
        fold_paper = fold(fold_paper, axis, int(val))
    
    result = np.where(fold_paper<1,' ','#')
    string_result = ""
    for line in result.transpose():
        string_result += "".join([str(x) for x in line])+"\n"
    return string_result

def fold(paper, axis, position):
    if axis == 'x':
        fold_1 = paper[:position,:]
        fold_2 = np.flipud(paper[position+1:,:])
    if axis == 'y':
        fold_1 = paper[:,:position]
        fold_2 = np.fliplr(paper[:,position+1:])
    return np.clip(fold_1+fold_2, 0, 1)

if __name__ == "__main__":
    day = 13
    points, folds = get_input(day, splitlines=False).split('\n\n')
    points = [[int(x) for x in p.split(',')] for p in points.splitlines()]
    folds = [f.split('along ')[1].split('=') for f in folds.splitlines()]
    print(part1(points, folds))
    print(part2(points, folds))

