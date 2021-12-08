from utils import get_input
import itertools
import numpy as np

def part1(output_values):
    s = 0
    for line in output_values:
        for el in line:
            if len(el) in [2,3,4,7]:
                s+=1
    return s

def part2(input_values, output_values):
    numbers = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7,
         "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}
    numbers = {"".join(sorted(key)):val for key,val in numbers.items()}
    ans = 0

    for i in range(len(output_values)): 
        for p in itertools.permutations(['a','b','c','d','e','f','g']):
            perm = {key:value for key,value in zip(p,['a','b','c','d','e','f','g'])}
            perm_input = ["".join(perm[char] for char in x) for x in input_values[i]]
            perm_output = ["".join(perm[char] for char in x) for x in output_values[i]]
            matches = True
            for perm_in in perm_input: # check that all numbers are in input
                if "".join(sorted(perm_in)) not in numbers:
                    matches = False
                    break
            if matches: 
                perm_output = ["".join(sorted(x)) for x in perm_output]
                ans += int("".join(str(numbers[x]) for x in perm_output))
                break

    return ans

if __name__ == "__main__":
    day = 8
    data = [x.split(' | ') for x in get_input(day)]
    input_values = [x[0].split(' ') for x in data]
    output_values = [x[1].split(' ') for x in data]
    print(part1(output_values))
    print(part2(input_values, output_values))