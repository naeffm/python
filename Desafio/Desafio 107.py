import moeda

p = float(input('Digite um valor em R$ '))

print(f'a metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Diminuido 13%, temos {moeda.diminuir(p,13)}')