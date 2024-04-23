num = [2,5,9,1]
print(num)

num[2] = 3 #adicionando um elemto no lugar do outro

print(num)

num.append(7) #adicionando elementos da forma correta
num.sort() #deixando tudo na ordem crescente
num.insert(2,2) #adicionando valor sem substituir o outro
num.pop() #remover o ultimo elemento
num.remove(2) #nesse caso que possui 2 numeros 2, ele remove o primeiro do contador
if 4 in num:
    num.remove(4)
else:
    print('nao achei o numero 4')

print(num)

print(f'essa lista tem {len(num)} elementos')

valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('cheguei o final da lista')

mano = []

#for cont in range(0,5):
#    mano.append(int(input('Digite um valor: ')))

print('#' *100)

a = [2,3,4,7]
b = a
b[2] = 8
print(a)
print(b) #a partir de que colocamos igual, o python entende uma ligacao entre elas.
print('#' *100)

k = [2,3,4,7]
l =k[:]
l[2] = 8
print(k)
print(l)