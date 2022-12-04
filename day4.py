from functions import text_parser

if __name__ == "__main__":
    raw_data = text_parser('day4.txt')
    
    # part 1
    count = 0
    for line in raw_data:
        a,b = line.split(',')
        a,b = a.split('-'), b.split('-')
        a,b = [int(x) for x in a], [int(x) for x in b]
    
        if ((a[0] >= b[0]) & (a[1] <= b[1])) | ((b[0] >= a[0]) & (b[1] <= a[1])):
            count += 1
    print(count)

    # part 2
    count = 0
    for line in raw_data:
        a,b = line.split(',')
        a,b = a.split('-'), b.split('-')
        a,b = [int(x) for x in a], [int(x) for x in b]
        if b[0] < a[0]:
            a,b = b,a

        if (a[0] <= b[0]) & (b[0] <= a[1]):
            count += 1
    print(count)

