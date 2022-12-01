from functions import text_parser

if __name__ == "__main__":
    raw_data = text_parser('day1_1.txt')
    
    # part 1
    m = 0
    c = 0
    for n in raw_data:
        if n == '':
            m = max(m, c)
            c = 0
        else:
            c += int(n)
    print(m)

    # part 2
    elves = [0]
    for n in raw_data:
        if n == '':
            elves.append(0)
        else:
            elves[-1] += int(n)
    elves.sort()
    print(sum(elves[-3:]))
