from utils import get_input

def part1(numbers, boards):
    for i in range(len(numbers)):
        drawn = numbers[:i]
        winner_board = get_winner(numbers[:i], boards)
        if winner_board:
            return get_score(drawn, winner_board)

def get_winner(drawn, boards):
    found_winner = False
    for board in boards:
        board_transposed = list(map(list, zip(*board)))
        for b in [board, board_transposed]:
            for line in b:
                found_in_line = True
                for number in line:
                    if number not in drawn:
                        found_in_line = False
                        break
                if found_in_line:
                    return board
    return None

def get_score(drawn, board):
    s = 0
    for line in board:
        for number in line:
            if number not in drawn:
                s += int(number)
    return s * int(drawn[-1])

def get_winners(drawn, boards):
    found_winner = False
    winners = []
    for board in boards:
        board_transposed = list(map(list, zip(*board)))
        for b in [board, board_transposed]:
            for line in b:
                found_in_line = True
                for number in line:
                    if number not in drawn:
                        found_in_line = False
                        break
                if found_in_line:
                    if board not in winners:
                        winners.append(board)
    return winners


def part2(numbers, boards):
    for i in range(len(numbers)):
        drawn = numbers[:i]
        for winner_board in get_winners(numbers[:i], boards):
            boards.remove(winner_board)
            if len(boards) == 0:
                return get_score(drawn, winner_board)

def process_data(data):
    numbers = data[0].split(",")
    boards = []
    for i in range(round(len(data[2:])/6)):
        boards.append([x.split() for x in data[2+6*i:7+6*i]])
    return numbers, boards

if __name__ == "__main__":
    day = 4
    data = get_input(day)
    numbers, boards = process_data(data)
    print(part1(numbers, boards))
    print(part2(numbers, boards))

