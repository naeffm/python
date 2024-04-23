teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) #adicionamos a primeira

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:]) #adicionamos a segunda por isso 2

print(galera)

print('-'*50)

mossada = [['Naeff',21], ['Vitor',22], ['Barroncas',19], ['Rafael',23]]
print(mossada[2][1])
print('-'*50)
for p in mossada:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-'*50)

teste = list()
teste2 = list()

for c in range(0,3):
    teste2.append(str(input('nome: ')))
    teste2.append(int(input('idade: ')))
    teste.append(teste2[:])
    teste2.clear()

print('-'*50)
totalma = totalmen = 0
for j in teste:
    if j[1] >= 21:
        print(f'{j[0]} é maior de idade')
        totalma += 1
    else:
        print(f'{j[0]} menor de idade')
        totalmen += 1
print('-'*50)