a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print()

#o que queremos
#soma(4,5)
#soma(8,9)
#soma(2,1)

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(4,5)

print()

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 8, 2)

print()

valores = [7,2,5,0,4]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)
    
dobra(valores)
