from utils import get_input

def part1(data):
    sfsum = data[0]
    for sfnum in data[1:]:
        sfsum = add(sfsum, sfnum)
        sfsum = reduce(sfsum)
    return magnitude(eval(sfsum))

def part2(data):
    m = 0
    for num1 in data:
        for num2 in data:
            m = max(part1([num1,num2]),m)
    return m

def add(exp_a, exp_b):
    return '[' + exp_a + ',' + exp_b + ']'

def reduce(expression):
    explodes, splits = True, True
    while explodes or splits:
        explodes, splits = False, False
        depth = 0
        for i in range(len(expression)):
            if expression[i] == ']':
                depth -= 1
            elif expression[i] == '[':
                depth += 1
                if expression[i+2] == ']':
                    print("error")
                    return None
                if depth == 5:
                    explodes = True
                    break
        if explodes:
            expression = explode(expression, i)
            continue

        for i in range(len(expression)):
            if expression[i].isnumeric():
                k = 1
                while expression[i:i+k+1].isnumeric():
                    k += 1
                if k > 1: # 2 digits => num>=10
                    expression = split(expression, i, k)
                    splits = True
                    break

    return expression

def explode(expression, idx):
    
    k_a = 1
    while expression[idx+1:idx+k_a+1].isnumeric():
        k_a += 1
    a = int(expression[idx+1:idx+k_a])

    idx_b = idx+k_a+1
    k_b = 1
    while expression[idx_b:idx_b+k_b+1].isnumeric():
        k_b += 1
    b = int(expression[idx_b:idx_b+k_b])
    new_expression = expression[:idx]+'0'+expression[idx_b+k_b+1:]
    
    #print("explode",expression,"at",expression[idx:idx_b+k_b+1])

    i = idx - 1
    while i > 0:
        i -= 1
        if new_expression[i].isnumeric():
            k = 0
            while new_expression[i-k-1:i+1].isnumeric():
                k += 1
            c = int(new_expression[i-k:i+1])+a
            new_expression = new_expression[:i-k]+str(c)+new_expression[i+max(k,1):]
            break
    j = idx + 1
    while j < len(new_expression)-1:
        j += 1
        if new_expression[j].isnumeric():
            k = 1
            while new_expression[j:j+k+1].isnumeric():
                k += 1
            d = int(new_expression[j:j+k])+b
            new_expression = new_expression[:j]+str(d)+new_expression[j+k:]
            break

    #print(new_expression)
    return new_expression

def split(expression, idx, k):
    num_to_split = int(expression[idx:idx+k])
    a = num_to_split // 2
    b = num_to_split // 2 + num_to_split % 2
    return expression[:idx] + "[" + str(a) + "," + str(b) + "]" + expression[idx+k:]

def magnitude(expression):
    if isinstance(expression, int):
        return expression
    return 3*magnitude(expression[0])+2*magnitude(expression[1])

if __name__ == "__main__":
    day = 18
    data = get_input(day)
    print(part1(data))
    print(part2(data))

