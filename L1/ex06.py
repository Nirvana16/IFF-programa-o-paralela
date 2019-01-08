'''
Considere dois números inteiros a e b (b ≥ 0) lidos pelo teclado. Faça um
algoritmo recursivo para calcular o valor de ab.
'''

def calcularExp(a, b):
    if b > 0:
        return a*calcularExp(a, b-1)
    else:
        return 1

def main():
    #usa o Eval para que o python trate o valor lido como um numero q possa ser passado via parametro na função calcular expoente
    valor_a = int(input("Digite o valor de a \n"))
    valor_b = int(input("Digite o valor de b \n"))
    print(calcularExp(valor_a, valor_b))

main()
