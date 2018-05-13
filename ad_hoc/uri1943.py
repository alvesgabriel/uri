def top_collocation(k):
    if k == 1:
        return 'Top 1'
    if k <= 3:
        return 'Top 3'
    if k <= 5:
        return 'Top 5'
    if k <= 10:
        return 'Top 10'
    if k <= 25:
        return 'Top 25'
    if k <= 50:
        return 'Top 50'
    if k <= 100:
        return 'Top 100'


def main():
    k = int(input().strip())
    print(top_collocation(k))

if __name__ == '__main__':
    main()