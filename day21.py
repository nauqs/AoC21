from utils import *

def part1(start_p1, start_p2):

    i = 1
    s1, s2, p1, p2 = 0, 0, start_p1, start_p2

    while s1<1000 and s2<1000:           
        die, i = throw_die(i)
        p1 = (p1 + die - 1) % 10 + 1
        s1 += p1
        if s1>=1000: break
        die, i = throw_die(i)
        p2 = (p2 + die - 1) % 10 + 1
        s2 += p2
        if s2>=1000: break

    return min(s1,s2)*(i-1)

def throw_die(i):
    die = 0
    for _ in range(3):
        die += (i - 1) % 100 + 1
        i += 1
    return die, i

def part2(start_p1, start_p2):
    return max(simulate(start_p1, start_p2, 0, 0, 1))

# no need to simulate all 27 universes, as sum of 1,2,3 can only be 7 different values
die_counts = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1} # ty ADIP

def simulate(start_p1, start_p2, start_s1, start_s2, turn):

    wins1, wins2 = 0, 0
    
    for die in die_counts:
        s1, s2, p1, p2 = start_s1, start_s2, start_p1, start_p2

        if turn == 1:
            p1 = (p1 + die - 1) % 10 + 1
            s1 += p1
            if s1 >= 21: wins1 += die_counts[die]
            else:
                extra_wins1, extra_wins2 = simulate(p1, p2, s1, s2, 2)
                wins1 += extra_wins1 * die_counts[die]
                wins2 += extra_wins2 * die_counts[die]

        if turn == 2:
            p2 = (p2 + die - 1) % 10 + 1
            s2 += p2
            if s2 >= 21: wins2 += die_counts[die]
            else:
                extra_wins1, extra_wins2 = simulate(p1, p2, s1, s2, 1)
                wins1 += extra_wins1 * die_counts[die]
                wins2 += extra_wins2 * die_counts[die]

    return wins1, wins2

if __name__ == "__main__":
    day = 21
    p1, p2 = 8, 4
    print(part1(p1, p2))
    print(part2(p1, p2))
