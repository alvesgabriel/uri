def square_2(n):
    if n == 0:
        return 0
    return 1 / (2 + square_2(n - 1))

def main():
    n = int(input().strip())
    print('%.10f' % (1 + square_2(n)))

if __name__ == '__main__':
    main()