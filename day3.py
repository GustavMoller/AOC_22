from functions import text_parser, get_priority

if __name__ == "__main__":
    raw_data = text_parser('day3.txt')
    
    # part 1
    count = 0
    for line in raw_data:
        m = int(len(line)/2)
        c1, c2 = line[:m], line[m:]
        count += get_priority([x for x in c1 if x in c2][-1])
    print(count)

    # part 2
    count = 0
    for line1, line2, line3 in list(zip(raw_data[::3], raw_data[1::3], raw_data[2::3])):
        count += get_priority([x for x in line1 if x in line2 and x in line3][-1])
    print(count)

