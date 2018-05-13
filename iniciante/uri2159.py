import math

n = int(input().strip())

p = n / math.log(n)
m = 1.25506*p

print('%.1f %.1f' % (p, m))