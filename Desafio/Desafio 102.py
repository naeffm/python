def fatorial(num=1,show=False):
    f = 1
    for c in range(num,0,-1):
        if show==True:
           print(c, end='')
           if c > 1:
              print(' x ', end='')
           else:
              print(' = ', end='')
        f *= c
    return f
    
    """
    -> Calcula o fatorial de um número.
    :param n: O numero a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um numero n.
    """
            
print(fatorial(5,show=True))