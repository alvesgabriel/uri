def rpm(r):
    if len(r) <= 1:
        return 0
    for i in range(1, len(r)):
        if r[i-1] > r[i]:
            return i + 1
    return 0

def main():
    n = int(input().strip())
    r = tuple(int(_) for _ in input().strip().split())
    print(rpm(r))

if __name__ == '__main__':
    main()