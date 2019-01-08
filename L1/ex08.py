'''
Considere o arquivo “Numeros.txt” com 20 números inteiros que devem ser
armazenados em um vetor. Faça um algoritmo recursivo para imprimir o maior
valor deste vetor.
Obs.: Não é permitido utilizar qualquer outro vetor/matriz para auxiliar.
'''
from random import randrange

N = 20

def gerarVetor():
    global numeros
    arquivo = open("Numeros.txt", 'w')
    numeros = [randrange(1, 21)for i in range(N)]
    arquivo.write(str(numeros))
    arquivo.close()

def lerVetor():
    vetor = [0 for i in range(N)]
    arquivo = open("Numeros.txt", 'r')
    arquivo = arquivo.read()
    arquivo = arquivo.replace("[", "")
    arquivo = arquivo.replace("]", "")
    arquivo = arquivo.split(",")
    for i in range(N):
        vetor[i] = int(arquivo[i])
    return vetor

def maior(n,t):
    if 0 <= t:
        v = maior(n, t-1)
        if v<n[t]:
            return(n[t])
        else:
            return v
    else:
        return 0


def main():
    gerarVetor()
    vetor2 = lerVetor()
    print(vetor2)
    m = maior(vetor2, N-1)
    print(m)


main()
