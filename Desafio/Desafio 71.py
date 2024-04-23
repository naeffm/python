print("------------------------------")
print("       CAIXA ELETRONICO")
print("------------------------------")

nota50 = 0
nota501 = 0
gostoso = 0
nota20 = 0
nota10 = 0
nota1 = 0
cont = 0
nota2 = 0

while True:
    valor = int(input('QUANTO VOCÊ QUER SACAR R$ '))
    u = valor // 1 % 10
    d = valor // 10 % 10
    c = valor // 100 % 10
    m = valor // 1000 % 10
    if m > 0:
        m *= 1000
        nota50 = m / 50
    if c > 0:
        c *= 100
        nota501 = c / 50
    if d > 0:
        d *= 10
        if d % 20 == 0:
            nota20 = d / 20
        else:
            if d % 20 != 0:
                nota20 = (d / 20) - 0.5
                nota2 = d - (20 * nota20)
                nota10 = nota2 / 10


    if u > 0:
        nota1 = u

    gostoso = nota50 + nota501

    break

print(f'AQUI TEM {gostoso:.0f} DE cinquenta')
print(f'AQUI TEM {nota20:.0f} DE vinte')
print(f'AQUI TEM {nota10:.0f} DE dez')
print(f'AQUI TEM {nota1:.0f} DE um')

# 50, 20, 10, 1