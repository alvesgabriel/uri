n = input()
l = map(int, input().strip().split())

s = {2: 0, 3: 0, 4: 0, 5: 0, }
for i in l:
    if i % 2 == 0:
        s[2] += 1
    if i % 3 == 0:
        s[3] += 1
    if i % 4 == 0:
        s[4] += 1
    if i % 5 == 0:
        s[5] += 1

for i, v in s.items():
    print('%d Multiplo(s) de %d' % (v, i))

