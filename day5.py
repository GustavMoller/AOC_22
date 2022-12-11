from functions import text_parser
import re

if __name__ == "__main__":
    raw_data = text_parser('day5.txt')
    
    # part 1

    # we iterate over the input and initialize the stack
    n_cols = int((len(raw_data[0])+1)/4)
    stacks = {i:[] for i in range(1, n_cols+1)}
    for line in raw_data:
        if "1" in line:
            break
        else:
            for i in range(1, n_cols+1):
                char = line[(i-1)*4+1]
                if char != " ":
                    stacks[i].append(char)

    # we invert all the stacks
    for i in stacks.keys():
        stacks[i].reverse()

    # we follow the instructions
    for line in raw_data:
        if "move" not in line:
            continue
        a,b,c = map(int, re.findall(r'\d+', line))
        for _ in range(a):
            stacks[c].append(stacks[b].pop())

    # obtain output
    out = ""
    for i,stack in stacks.items():
        out+=stack[-1]

    # part 2

    # we iterate over the input and initialize the stack
    n_cols = int((len(raw_data[0])+1)/4)
    stacks = {i:[] for i in range(1, n_cols+1)}
    for line in raw_data:
        if "1" in line:
            break
        else:
            for i in range(1, n_cols+1):
                char = line[(i-1)*4+1]
                if char != " ":
                    stacks[i].append(char)

    # we invert all the stacks
    for i in stacks.keys():
        stacks[i].reverse()

    # we follow the instructions
    for line in raw_data:
        if "move" not in line:
            continue
        a,b,c = map(int, re.findall(r'\d+', line))
        for _ in range(a):
            stacks[c].append(stacks[b].pop())
        stacks[c][-a:] = stacks[c][-a:][::-1]    

    # obtain output
    out = ""
    for i,stack in stacks.items():
        out+=stack[-1]

    print(out)

