lista = []

for c in range (0,5):
    num = int(input('Digite um numero: '))
    lista.append(num)

print(f'O maior valor é {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor é {min(lista)} na posição {lista.index(min(lista))}')

