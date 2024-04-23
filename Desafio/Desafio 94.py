cadastro = dict()
princ = list()
soma = 0
maior = list()

while True:
    
    cadastro['nome'] = str(input('nome: '))
    cadastro['sexo'] = str(input('sexo M/F: ')).upper()
    cadastro['idade'] = int(input('idade: '))
    soma += cadastro['idade']
    princ.append(cadastro.copy())
    

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N: ')).upper()
    if resp == 'N':
        break

print(f'A) {len(princ)}')
media = soma / len(princ)
print(f'B) {media:.2f}')
print(f'C)',end=' ')

for p in princ:
    if p['sexo'] == 'F': #eu consigo usar um filtro de dicinionario mesmo estando em uma lista
        print(p['nome'], end=' ')
print()
print('D) ',end='')
for p in princ:
    if p['idade'] > media:
        print(f'{p["nome"]}', end=' ')