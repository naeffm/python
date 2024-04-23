tupla = ('tabaco', 10,'açucar', 15,'vela7dias', 10,'alguidar',5)
print('-'*30)
print('     LISTAGEM DE PREÇOS   ')
print('-'*30)

for pos,cont in enumerate(tupla):
    pos +=1

    if pos % 2 != 0:
        print(f'{cont:.<15}',end='') #esse ':.<15' faz com que sempre tenham 15 caracteres daquele alinhados, como mostra no resutador, louco ne?

    if pos % 2 == 0:
        print(f'R$ {cont}')

print('-'*30)




