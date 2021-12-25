from utils import get_input
from collections import defaultdict


def recursive_validator(digits, z, i):

    if i == 14:
        if z != 0: return False
        valid.append(digits)
        return True

    branches = get_branches(z, i)
    for w in branches:
        recursive_validator(digits+str(w), monad_block(w, z, i), i+1)

def get_branches(z, i):
    """
    avoid blocks that multiply by 26 after dividing by 26
    """
    a, b = monad[i]
    if a > 0: # branch all digits
        return range(9,0,-1)
    else: # prune if x outside (1-9) range
        x = (z % 26) + a
        if 1 <= x <= 9:
            return range(x,x+1)
    return []

def monad_block(w, z, i):
    a, b = monad[i]
    x = int((z % 26) + a != w)
    if a <= 0: 
        z //= 26 # when a > 0, always divide by 1
    if not x: 
        return z
    return z * 26 + (x * (w + b))

def extract_input(monad):
    """
    Only lines and 4, 5 and 15 are different for each block (only value changes)
    """
    L = 18
    monad_values = []
    for i in range(len(monad)//L):
        block = monad[L*i:L*(i+1)]
        monad_values.append((int(block[5].split()[2]), int(block[-3].split()[2])))
    return monad_values

if __name__ == "__main__":
    day = 24
    monad = extract_input(get_input(day))
    valid, pruned = [], defaultdict(set)
    recursive_validator('', 0, 0)
    print(min(valid))
    print(max(valid))

""" 
Naive brute force...

pos = {'w': 0, 'x':1, 'y':2, 'z':3}

def brute_force_part1(monad):
    N = 99999999999999
    numbers = 1111111111111
    best = 0
    wxyz = [0,0,0,0]
    for n in range(N-numbers,N):
        wxyz = brute_force_monad(monad, n)
        if wxyz[-1] == 0:
            print("ACCEPTED",n)
            best = max(best, n)
        if n%11111==0:
            print(n, wxyz)
    return best

def brute_force_monad(monad, number):
    wxyz = [0, 0, 0, 0]
    number = list(str(number))
    for line in monad:
        if line[:3] == 'inp':
            wxyz[pos[line.split(' ')[1]]] = int(number.pop(0))
        else:
            op_1, op_2 = line.split(' ')[1:]
            val_1 = wxyz[pos[op_1]]
            if op_2.lstrip('-').isdigit():
                val_2 = int(op_2)
            else:
                val_2 = wxyz[pos[op_2]]

            if line[:3] == 'add': 
                res = val_1 + val_2
            elif line[:3] == 'mul': 
                res = val_1 * val_2
            elif line[:3] == 'div': 
                res = val_1 // val_2
            elif line[:3] == 'mod': 
                res = val_1 % val_2
            elif line[:3] == 'eql': 
                res = int(val_1 == val_2)

            wxyz[pos[op_1]] = res

    return wxyz
"""
