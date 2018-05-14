def main():
    while True:
        try:
            n, m = (int(_) for _ in input().strip().split())
            models = list(int(_) for _ in input().strip().split())
            models.sort(reverse=True)
            total = sum(models[:m])
            print(total)
        except EOFError:
            break

if __name__ == '__main__':
    main()