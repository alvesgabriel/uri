from datetime import date

year = 2016
natal = date(year, 12, 25)

while True:
    try:
        month, day = (int(_) for _ in input().strip().split())
        if month == 12 and day == 25:
            print('E natal!')
        elif month == 12 and day == 24:
            print('E vespera de natal!')
        elif month == 12 and day > 25:
            print('Ja passou!')
        else:
            delta = natal - date(year, month, day)
            print('Faltam %d dias para o natal!' % delta.days)
    except EOFError:
        break