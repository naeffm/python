num = [2,5,9,1] #lista com pochet

num[2] = 3  #substituindo valor (na posição 2 por o 3)

#num[4] = 7 ERRADA tentativa de adicionar um num para lista

num.append(7) #COORRETO adicionando um novo elemnto a lista

num.sort() #coloca a lista em ordem

print(num.sort(reverse=True)) #coloca na ordem INVERSA

num.insert(2,0) #para inserir o 2 na posição 0

num.pop() #para remorer a posição entre parentese, nenhuma = ultima posição

num.remove(2) #tinha dois 2 na lista, esse comando so remove o primeiro

if 4 in num: #para caso nao saber se tem o numero 4, use if
    num.remove(4) #ele so removera o 4 quando tiver

print(num)

print(f'Essa lsita tem {len(num)} elementos')

print('-'*50)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: #para cada valor em valores
    print(f'{v}...')
print('#'*50)
for c, v in enumerate(valores): #para posição em cada valor
    print(f'na posição {c} encontrei o valor {v}')

for cont in range(0,5): #adicionando valores na lista com input
    valores.append(int(input('Digite algo: ')))

print(valores)

print('-'*30)

#PECULIARIDADE do python, ao adicionar um valor em uma lista que é igual a outra
#ele substitue esse valor para as duas listas que estao igualadas
a = [2,3,4,7]
b = a
b[2] = 8

print(a)
print(b)

#para isso nao acontecer o codigo é escrito dessa forma

b = a[:] # a[:] comando significa uma copia de algo