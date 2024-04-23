jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do perna de pau: ')) #inserimos em jogador o nome 
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #salvamos qnt de partiads em 'jogo'

for c in range(0, jogos): #identicamos qnts gols foram feitos em cada partida
    partidas.append(int(input(f' Quantos gols na {c+1}º partida : '))) #adicionamos os gols direto em partida com append* 

jogador['gols'] = partidas[:] #jogamos os gols em partidas para o dicinioario
jogador['total'] = sum(partidas) #salvamos o total de gols no dicinionari como total

print('-='*30)
print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem valor {v}')
print('-='*30)

print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.') #a qnt de gols é o numero de partidas não?!
for i, v in enumerate(partidas):
    print(f'na {i+1}º partida fez {v} gols. ')
print(f'na soma de tudo ele fez {jogador["total"]} gols.')
print('-='*30)