from utils import get_input
from collections import defaultdict

def simulate_steps(template, rules, n):

    drules, template_counter, letter_counter = defaultdict(str, rules), defaultdict(int), defaultdict(int)
    for i in range(len(template)-1):
        template_counter[template[i:i+2]] += 1
        letter_counter[template[i]] += 1
    letter_counter[template[-1]] += 1

    for step in range(n):
        new_counter = defaultdict(int)
        for pair in template_counter:
            n = template_counter[pair]
            result = drules[pair]
            if result != '':
                new_counter[pair[0]+result] += n
                new_counter[result+pair[1]] += n
                letter_counter[result] += n
        template_counter = new_counter

    return max(letter_counter.values())-min(letter_counter.values())

def part1(template, rules):
    return simulate_steps(template, rules, 10)

def part2(template, rules):
    return simulate_steps(template, rules, 40)

if __name__ == "__main__":
    day = 14
    data = get_input(day)
    template = data[0]
    rules = {pair: result for pair, result in [x.split(' -> ') for x in data[2:]]}
    print(part1(template, rules))
    print(part2(template, rules))

