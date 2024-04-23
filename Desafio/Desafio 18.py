import math
angulo = float(input('Digie o angul que você deseja '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o seno de {:.2f} {} {}'.format(angulo, seno, cosseno, tangente))

# Esse math.radians seve para mudar o radians para graus
# Como o comando vem de origem transofrmando em radians