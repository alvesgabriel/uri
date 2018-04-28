n, m = map(int, input().strip().split())

for i in range(m):
    inp = input()
    if inp == 'clicou':
        n -= 1
    elif inp == 'fechou':
        n += 1
print(n)