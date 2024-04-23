def ficha():
    nome = str(input('Qual seu nome jogador: '))
    gols = input('Quantos gols foram feitos: ')
    if nome == '':
        print('desconhecido fez ',end='')
    else:
        print(f'{nome} fez ',end='')
    if gols.isnumeric() :
        gols = int(gols)
        print(f'{gols} gols no campeonato')
    else:
        gols = 0
        print(f'{gols} gols no campeonato')
        
ficha()