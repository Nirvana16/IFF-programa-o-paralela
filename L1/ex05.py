'''
Considere um número inteiro n (n ≥ 0) lido pelo teclado. Faça um algoritmo
recursivo para calcular o fatorial de n.
'''

def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return n*fatorial(n-1)

def main():
    numero = eval(input("Digite um número\n"))
    numero = fatorial(numero)
    print(numero)

main()


