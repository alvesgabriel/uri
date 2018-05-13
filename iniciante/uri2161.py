def square_10(n):
    if n == 0:
        return 0
    return 1 / (6 + square_10(n - 1))

def main():
    n = int(input().strip())
    print('%.10f' % (3 + square_10(n)))

if __name__ == '__main__':
    main()