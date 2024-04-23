dados = list()
pessoas = list()

dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
print('-'*50)

pessoas.append(dados[:]) #adicionamos a copia da lista dados

print(pessoas)
print('-'*50)
exemplo = [['Pedro',25], ['Maria',19],['João',32]]

print(exemplo)
print('-'*50)
print(exemplo[0][0]) #primeiro zero é para identificar a lista, o segundo zero para identificar qual elemento dessa lista
print(exemplo[1][1])
print(exemplo[1])
print('-'*50)