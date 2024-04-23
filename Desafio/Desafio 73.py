time = ('PALMEIRAS', 'INTER', 'FLUMINENSE', 'CORINTHIAS', 'FLAMENGO', 'ATLETICO-PR', 'ATLETICO-MG','FORTALEZA','SAO PAULO','AMERICA', 'BOTAFOGO','SANTOS','GOIAS','treze','CHAPECO','quinze','dezesseis','BARCELONA','REAL','MANCHESTER C','PSG')

print('LETRA A)')
for cont in range(0, 5):
    print(f'{cont+1}° {time[cont]}')
print('LETRA B)')
print(time[-4:])
print('LETRA C)')
print(sorted(time))
print('LETRA D)')
x = time.index('CHAPECO')
print(x)