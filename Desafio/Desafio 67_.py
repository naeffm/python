n1 = int(input('Digite qual numero você quer a tabuada: '))
t = 0
total = 0


while True:
    while t < 10:
        t += 1
        print(f'{n1} x {t} = {n1 * t}')
    n1 = int(input('Qual agora: '))
    t = t - 10
    if n1 < 0:
        break
print('THE END')












