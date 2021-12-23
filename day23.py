from utils import get_input
import copy

correct = {'A':0,'B':1,'C':2,'D':3, '.':-1}
hallway_pos = {'H1':(1,1), 'H2':(1,2), 'H3':(1,4), 'H4':(1,6), 'H5':(1,8), 'H6':(1,10), 'H7':(1,11)}

instructions = """
---------------------------------------------
Instructions:
       12 3 4 5 67
      #############
 H -> #...........#
 1 -> ###.#.#.#.###
 2 ->   #.#.#.#.#
        #########
         A B C D
Enter: ~origin~ ~destination~, (e.g. 'A1 H1')
'restart' to start over
--------------------------------------------"""

def part1(data):

    print("\n WELCOME TO THE AMPHIMOD GAME!\n")
    print(instructions)

    room_map = [list(line) for line in data.copy()]

    energy = 0
    ordered = False

    while not ordered:

        # Print map and get input
        print_map(room_map)
        string = input()
        string = string.upper()

        # Special inputs and check format
        if string == "restart": return -1
        if string == "instructions":
            print(instructions)
            continue
        if not correct_format(string):
            continue

        # If input correct, perform moves
        origin, dest = string.split(' ')

        # Hallway origin
        if origin[0]=='H':
            o_row, o_col = hallway_pos[origin]
        else:
            o_row, o_col = room_pos(origin)

        amphimod = room_map[o_row][o_col]
        if amphimod not in ['A','B','C','D']:
            print("Wrong positions")
            continue
        
        if dest[0] == 'H':
            row, col = hallway_pos[dest]
            if room_map[row][col] != '.':
                print("Wrong positions")
                continue  
            room_map[o_row][o_col] = '.'
            room_map[row][col] = amphimod
        else:
            row, col = room_pos(dest)
            if room_map[row][col] != '.':
                print("Wrong positions")
                continue
            room_map[o_row][o_col] = '.'
            room_map[row][col] = amphimod

        if o_row == 1 or row == 1:
            distance = abs(row-o_row) + abs(col-o_col)
        else:
            distance = abs(row-1) + abs(o_row-1) + abs(col-o_col)

        step_energy = distance  * (10 ** correct[amphimod])

        energy += step_energy
        print("Current energy:", energy)
        ordered = check_ordered(room_map)

    print("YOU WON!")

    return energy

def room_pos(string):
    return int(string[1])+1, 3+2*correct[string[0]]

def correct_format(string):
    try:
        origin, dest = string.split(' ')
    except:
        print("Two positions expected' (e.g. 'A1 H1')")
        return False
    if not (len(origin)==2 and len(dest)==2):
        print("The format must be  '~origin~ ~destination~' (e.g. 'A1 H1')")
        return False
    if not (origin[0] in ['H','A','B','C','D'] and dest[0] in ['H','A','B','C','D']):
        print("The format must be  '~origin~ ~destination~' (e.g. 'A1 H1')")
        return False
    if not (origin[1].isdigit() and dest[1].isdigit()):
        print("The format must be  '~origin~ ~destination~' (e.g. 'A1 H1')")
        return False
    for inp in [origin, dest]:
        if inp[0]=='H':
            if int(inp[1]) not in range(1,8):
                print("Hallway positions go from 1 to 7")
                return False
        else:
            if int(inp[1]) not in range(1,3):
                print("Room positions go from 1 to 2")
                return False
    return True

def print_map(room_map):
    print("\n")
    for line in room_map:
        print("".join(line))

def check_ordered(room_map):
    for i in range(4):
        if not (correct[room_map[2][3+2*i]]==i):
            return False
        if not (correct[room_map[3][3+2*i]]==i):
            return False
    return True

def part2(positions):
    return 0

def process_input(data):
    positions = []
    for i in range(4):
        room = []
        room.append(data[2][3+2*i])
        room.append(data[3][3+2*i])
        positions.append(room)
    return positions

if __name__ == "__main__":
    day = 23
    data = get_input(day)
    data = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
  """.splitlines()
    data = get_input(day)
    positions = process_input(data)
    result = part1(data)
    if result ==-1:
        part1(data)
    else:
        print("\nEnergy:", result, "\n")

    #print(part2(copy.deepcopy(data)))

