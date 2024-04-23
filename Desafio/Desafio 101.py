def voto(num=0):
    from datetime import date
    atual = date.today().year
    idade = atual - num
    if atual - num >= 18 and 2023 - num < 65:
        return f'com {idade} anos, pode votar'
    if atual - num >= 16 and 2023 - num < 18:
        return f'com {idade} anos, tem voto opcional'
    if atual - num < 16:
        return f'com {idade} anos, nao pode votar'
    if atual - num >= 65:
        return f'com {idade} anos, o voto é opcional'

n = int(input('Em que ano você nasceu: '))
print(voto(n))