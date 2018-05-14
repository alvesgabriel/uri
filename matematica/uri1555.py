def rafael(x, y):
    return ((3 * x) ** 2) + (y ** 2)

def beto(x, y):
    return (2 * (x ** 2)) + ((5 * y) ** 2)

def carlos(x, y):
    return (-100 * x) + (y ** 3)

def main():
    n = int(input().strip())
    for i in range(n):
        x, y = (int(_) for _ in input().strip().split())
        func = {
            'Rafael': rafael(x, y),
            'Beto': beto(x, y),
            'Carlos': carlos(x, y),
        }
        winner = max(func.items(), key=lambda t: t[1])
        print('%s ganhou' % winner[0])

if __name__ == '__main__':
    main()