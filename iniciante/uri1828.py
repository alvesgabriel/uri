text = {
    'sheldon': 'Bazinga',
    'raj': 'Raj trapaceou',
    'draw': 'De novo',
}

win = {
    'tesoura': ('papel', 'lagarto'),
    'papel': ('pedra', 'Spock'),
    'pedra': ('lagarto', 'tesoura'),
    'lagarto': ('Spock', 'papel'),
    'Spock': ('tesoura', 'pedra'),
}

t = int(input())

for i in range(1, t + 1):
    sheldon, raj = input().strip().split()
    if sheldon == raj:
        print('Caso #%d: %s!' % (i, text['draw']))
    elif raj in win[sheldon]:
        print('Caso #%d: %s!' % (i, text['sheldon']))
    else:
        print('Caso #%d: %s!' % (i, text['raj']))