i = 1
while True:
    try:
        n1 = input()
        n2 = input()
        qtd = n2.count(n1)
        index = n2.rfind(n1) + 1
        print('Caso #%d' % i)
        if qtd and index != -1:
            print('Qtd.Subsequencias: %d' % qtd)
            print('Pos: %d' % index)
        else:
            print('Nao existe subsequencia')
        print()

        i += 1
    except EOFError:
        break