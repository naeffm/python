lanche = ('Hamburguer', 'Suco', 'Pizza', 'pudim')

#tuplas sao imutaveis (não se pode mudar)

print(lanche[1:3]) #vai do 1 até o 3

print(sorted(lanche)) #sorted coloca os itens em ordem

print(lanche[1:]) #vai do 1 até o final

print(lanche[:2]) #vai mostrar até chegar no 2 dai para

print(lanche[-3:]) #contando de trás para frente vai do -3 até final

print(len(lanche)) #len mostra a quantidade de itens da tupla

print('---------------------')

for cont in range(0, len(lanche)):
    print(cont)

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida}, na posição {pos}')

a = (2,5,4)
b = (5,8,1,2)
c = a + b

print(a)

print(b)

print(c)

print(len(c))

print(c.count(5)) #quantas vezes o elemento se repete

print(c.index(8)) #em qual posição está o numero entre parentese

print(c.index(5,1)) #este 1 significa o segundo numero 5 o primeiro 0

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #exclui uma tupla
print(pessoa)