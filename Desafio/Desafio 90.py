ex = dict()

ex['nome'] = str(input('nome: '))

ex['media'] = float(input(f'media de {ex["nome"]}: '))

if ex['media'] > 7:
    ex['situacao'] = 'APROVADO'
elif 5 > ex['media'] <=7:
    ex['situacao'] = 'RECUPERAÇÃO'
else:
    ex['situacao'] = 'REPROVADO'

for k,v in ex.items():
    print(f'O {k} é igual a {v}')