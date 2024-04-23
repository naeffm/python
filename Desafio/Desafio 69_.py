dezoito = 0
masculino = 0
mulheres20 = 0

while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('M/F: ')).upper()

    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        if idade < 20:
            mulheres20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N ? ')) .upper()
    if resp == 'N':
        break

print(f'A) {dezoito}  B) {masculino}  C) {mulheres20}')