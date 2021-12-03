from utils import get_input
import numpy as np

def part1(data):
    er_list = []
    for i in range(len(data[0])):
        er_list.append(str(round(sum([int(line[i]) for line in data])/len(data))))
    epsilon_rate = int("".join(er_list),2)
    gr_list = ['1' if x == '0' else '0' for x in er_list] 
    gamma_rate = int("".join(gr_list),2)
    return epsilon_rate*gamma_rate

def part2(data):
    o2_list = co2_list = []
    o2_opts = np.array(data)
    # Find oxgen rate
    for i in range(len(data[0])):
        col = [int(line[i]) for line in o2_opts]
        if sum(col)*2 == len(col):
            mask = np.array(col)==1
        else:
            most_common = round(sum(col)/len(col))
            mask = np.array(col)==most_common
        o2_opts = o2_opts[mask]
        if o2_opts.shape[0] == 1:
            break
    # Find CO2 rate
    co2_opts  = np.array(data)
    for i in range(len(data[0])):
        col = [int(line[i]) for line in co2_opts]
        if sum(col)*2 == len(col):
            mask = np.array(col)==0
        else:
            least_common = int(round(sum(col)/len(col))==0)
            mask = np.array(col)==least_common
        co2_opts = co2_opts[mask]
        if co2_opts.shape[0] == 1:
            break
    return int(o2_opts[0],2)*int(co2_opts[0],2)


if __name__ == "__main__":
    day = 3
    data = get_input(day)
    print(part1(data))
    print(part2(data))

