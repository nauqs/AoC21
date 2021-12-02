from utils import get_input

def part1(data):
    prev = 0
    data = [int(x) for x in data]
    c = -1
    for el in data:
      if prev<el:
        c+=1
      prev = el
    return c

def part2(data):
    prev = 0
    data = [int(x) for x in data]
    c=-1
    for i in range(len(data)-2):
      if prev< data[i]+data[i+1]+data[i+2]:
        c+=1
      prev = data[i]+data[i+1]+data[i+2]
    return c


if __name__ == "__main__":
    day = 1
    data = get_input(day)
    print(part1(data))
    print(part2(data))

