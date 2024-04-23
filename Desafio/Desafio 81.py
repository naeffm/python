lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N: ')).upper()
    if resp == 'N':
        break
print(lista)
print(len(lista))
lista.reverse()
print(lista)