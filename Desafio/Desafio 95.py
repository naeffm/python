dados = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do perna de pau: ')) #inserimos em jogador o nome 
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #salvamos qnt de partiads em 'jogo'

    partidas.clear()

    for c in range(0, jogos): #identicamos qnts gols foram feitos em cada partida
        partidas.append(int(input(f' Quantos gols na {c+1}º partida : '))) #adicionamos os gols direto em partida com append* 

    jogador['gols'] = partidas[:] #jogamos os gols em partidas para o dicinioario
    jogador['total'] = sum(partidas) #salvamos o total de gols no dicinionari como total

    dados.append(jogador.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N: ')).upper()
    if resp == 'N':
        break

print('-=' *30)

print('cod',end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()

print('-=' *30)

for k, v in enumerate(dados):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):>15}',end='')
    print()

print('-=' *30)

while True:
    busca = int(input('Mostar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {dados[busca] ["nome"]}:')
        for i, g in enumerate(dados[busca] ['gols']):
            print(f'   NO JOGO {i+1} fez {g} gols.')
    print('-=' *30)