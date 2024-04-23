segun = []
princ = []
contador = 0
maior = menor = 0

while True:
    segun.append(str(input('Digite seu nome: ')))
    segun.append(float(input('Qual seu peso: ')))

    if len(princ) == 0:
        maior = menor = segun[1] #possibilidade do primeiro caso, o primeiro numero registrado sera o menor e maior pois so tem ele
    else: #nao precisou por o len > 0 pois é else ja demonstra o caso de ter mais
        if segun[1] > maior:
            maior = segun[1]
        if segun[1] < menor:
            menor = segun[1]

    princ.append(segun[:])
    segun.clear()
    contador += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N: ')).upper()
    if resp == 'N':
        break

print(len(princ))
print(f'{maior} esse é o maior peso com nome: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print()
print(f'{menor} esse é o menor peso')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()