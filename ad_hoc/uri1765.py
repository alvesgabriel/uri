def calc_trapeze(b1, b2):
    return (b1 + b2) * 5 / 2

def ice_cream_used(q, b1, b2):
    return q * calc_trapeze(b1, b2)

def answer(i, ice_cream):
    return 'Size #%d:\nIce Cream Used: %.2f cm2' % (i, ice_cream)

def main():
    while True:
        t = int(input().strip())
        if t == 0:
            break
        for i in range(1, t + 1):
            q, a, b = (float(_) for _ in input().strip().split())
            ice_cream = ice_cream_used(q, a, b)
            print(answer(i, ice_cream))
        print()

if __name__ == '__main__':
    main()