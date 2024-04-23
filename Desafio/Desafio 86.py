valor = 0
banana1 = 0
banana2 = 0
listazero = []
listaum = []
listadois = []
contador = 0

while banana1 < 3:

    valor = int(input(f'Digite o valor para {banana1}:{banana2}: '))
    banana2 += 1
    contador += 1
    if banana2 == 3:
        banana1 += 1
        banana2 = 0
    if contador <= 3:
        listazero.append(valor)
    elif contador <= 6:
        listaum.append(valor)
    elif contador <= 9:
         listadois.append(valor)

print(listazero)
print(listaum)
print(listadois)

for num in listazero:
    print(f'[ {num} ]', end=' ')
print()
for num in listaum:
    print(f'[ {num} ]', end=' ')
print()
for num in listadois:
    print(f'[ {num} ]', end=' ')