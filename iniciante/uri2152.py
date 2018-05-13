t = int(input().strip())

for i in range(t):
    h, m, o = (int(_) for _ in input().strip().split())
    if o == 1:
        door = 'abriu'
    else:
        door = 'fechou'
    log = '%02d:%02d - A porta %s!' % (h, m, door)
    print(log)