lista = [] #criei uma lista vazia para adicionarmos

for cont in range(0,5):
    lista.append(int(input('Digite um valor: ')))

maior = max(lista)
menor = min(lista)

print(f'o maior numero é {maior} na {lista.index(maior)} posição')
print(f'o menor numero é {menor} na {lista.index(menor)} posição')