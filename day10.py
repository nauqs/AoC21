from utils import get_input
import numpy as np

def part1(data):
    s = 0
    points = {')':3, ']':57, '}':1197, '>':25137, '-':0}
    for line in data:
        s += points[parse1(line)]
    return s

def part2(data):
    incomplete_lines = []
    for line in data:
        if parse1(line) == '-':
            incomplete_lines.append(line)

    scores = []
    points = {'(':1, '[':2, '{':3, '<':4}
    for line in incomplete_lines:
        stack = parse2(line)
        s = 0
        while stack:
            s = s*5 + points[stack.pop()]
        scores.append(s)
    return sorted(scores)[len(scores)//2]

def parse1(line):
    stack = []
    openers, closers = ['(','{','[','<'], [')','}',']','>']
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            if stack.pop() != openers[closers.index(char)]:
                return char
    return '-'

def parse2(line):
    stack = []
    openers, closers = ['(','{','[','<'], [')','}',']','>']
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            assert stack.pop() == openers[closers.index(char)]
    return stack

if __name__ == "__main__":
    day = 10
    data = get_input(day)
    print(part1(data))
    print(part2(data))

