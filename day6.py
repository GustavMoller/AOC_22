from functions import text_parser
import re

if __name__ == "__main__":

    # part 1
    data = open(f'inputs/day6.txt', 'r').read()
    for i, chars in enumerate(zip(data, data[1:], data[2:], data[3:])):
        if len(set(chars)) == 4:
            print(i+4)
            break

    # part 2
    for i, chars in enumerate(zip(data, data[1:], data[2:], data[3:], data[4:], data[5:], data[6:], data[7:],
                                  data[8:], data[9:], data[10:], data[11:], data[12:], data[13:])):
        if len(set(chars)) == 14:
            print(i+14)
            break