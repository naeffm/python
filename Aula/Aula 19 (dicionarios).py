#tupla = ()
#lista = []
#dicionarios = {}

dados = list()
dados.append('Pedro')
dados.append(25)

print(dados)

#dados = dict()
dados = {'nome':'Pedro', 'idade': 25}

print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M' #não usamos mais o APPEND, agora adiciniomaos assim, ele automaticamente vai colocar no dicinario de dados

del dados['idade'] #como REMOVER a idade de dados

filme={'titulo':'Star Wars',
       'ano':1977,
       'diretor':'Geroge Lucas'
}

print(filme.values()) # ele ira mostrar tudo de filme, Star Wars, 1977, Geoge Lucas

print(filme.keys()) # com esse comando vamos mostrar o titulo, ano, diretor

print(filme.items()) # ele ira mostrar tanto o values quanto keys

for k,v in filme.items():
    print(f'o {k} é {v}')

print('#'*50)

locadora = []

locadora.append(filme)

print(locadora)

print(locadora[0]['ano'])
print(locadora[2]['titulo'])
