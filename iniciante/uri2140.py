bank_notes = (2, 5, 10, 20, 50, 100)

def is_possible(value):
    for n in bank_notes:
        value_copy = value - n
        if value_copy in bank_notes:
            return 'possible'
    return 'impossible'

while True:
    n, m = (int(_) for _ in input().strip().split())
    if n == m == 0:
        break
    print(is_possible(m - n))
