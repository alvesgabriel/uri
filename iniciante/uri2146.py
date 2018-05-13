while True:
    try:
        n = int(input().strip())
        print(n-1)
    except EOFError:
        break
