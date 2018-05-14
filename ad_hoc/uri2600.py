def is_classic_dice(*l):
    if l[0] + l[5] != 7:
        return False
    if l[1] + l[3] != 7:
        return False
    if l[2] + l[4] != 7:
        return False
    if sorted(l) != [1, 2, 3, 4, 5, 6]:
        return False
    return True

def main():
    n = int(input().strip())
    for i in range(n):
        l0 = int(input().strip())
        l1, l2, l3, l4 = (int(_) for _ in input().strip().split())
        l5 = int(input().strip())
        if is_classic_dice(l0, l1, l2, l3, l4, l5):
            print('SIM')
        else:
            print('NAO')

if __name__ == '__main__':
    main()