import moeda

p = float(input('Digite um valor em R$ '))

print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuido 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')