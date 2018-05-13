from itertools import zip_longest
import re

def sum_turing(a, b, c):
    s = str(int(a[::-1]) + int(b[::-1]))[::-1]
    zip_list = zip_longest(c, s, fillvalue='0')
    for t in zip_list:
        if t[0] != t[1]:
            return 'False'
    return 'True'

def main():
    while True:
        in_put = input().strip()
        a, b, c = re.findall(r'(\d+)', in_put)
        print(sum_turing(a, b, c))
        if a == b == '0':
            break

if __name__ == '__main__':
    main()