#tupla = ()
#lista = []
#dicionarios = {}

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas ['peso'] = 98.5 #adicionar sem usar o append

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #muito importante colocar em duas aspas para referenciar, porque ele já está em aspas simples

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

