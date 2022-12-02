from functions import text_parser

if __name__ == "__main__":
    raw_data = text_parser('day2.txt')
    
    # part 1
    score = 0
    for line in raw_data:
        if line == '':
            continue
        a = line.split()[0]
        b = line.split()[1]
        if b == 'X':
            score += 1
            if a == 'A':
                score += 3
            elif a == 'C':
                score += 6
        elif b == 'Y':
            score += 2
            if a == 'B':
                score += 3
            elif a == 'A':
                score += 6
        elif b == 'Z':
            score += 3
            if a == 'C':
                score += 3
            elif a == 'B':
                score += 6
    print(score)

    # part 2
    score = 0
    for line in raw_data:
        if line == '':
            continue
        a = line.split()[0]
        b = line.split()[1]
        if b == 'Z':
            score += 6
            if a == 'A':
                score += 2
            elif a == 'B':
                score += 3
            elif a == 'C':
                score += 1
        elif b == 'Y':
            score += 3
            if a == 'A':
                score += 1
            elif a == 'B':
                score += 2
            elif a == 'C':
                score += 3
        elif b == 'X':
            score += 0
            if a == 'A':
                score += 3
            elif a == 'B':
                score += 1
            elif a == 'C':
                score += 2
    print(score)
        