from utils import get_input

def part1(data):
    pos = [0,0]
    for el in data:
      ins, n = el.split()
      if ins == 'forward': pos[1]+= int(n)
      if ins == 'up': pos[0]-= int(n)
      if ins == 'down': pos[0]+= int(n)
    return pos[0]*pos[1]

def part2(data):
    aim, pos = 0, [0,0]
    for el in data:
      ins, n = el.split()
      if ins == 'up': aim-= int(n)
      if ins == 'down': aim+= int(n)
      if ins == 'forward': 
        pos[1]+= int(n)
        pos[0]+= aim*int(n)
    return pos[0]*pos[1]


if __name__ == "__main__":
    day = 2
    data = get_input(day)
    print(part1(data))
    print(part2(data))

