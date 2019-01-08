"""
Considere a Matriz A =[a]nxm, onde n = 4 e m = 5, com números inteiros
positivos gerados aleatoriamente de 1 até 20. Faça um algoritmo para gerar a matriz
A e verificar se ela satisfaz a seguinte condição: (ver na folha)
Crie um procedimento para gerar a matriz e uma função para realizar a
verificação. De acordo com o retorno da função de verificação, deve-se imprimir na
função main: “Condicao Satisfeita” ou “Condicao Nao Satisfeita”.

"""

from random import randrange

N = 4
M = 5

def gerarmatriz():
    global matrizA
    matrizA = [[randrange(1,21) for j in range(M)] for i in range(N)]

def verificar():
    minimo = 99999
    maximo = 0

    '''
    Encontrar valor minimo, o for vai varrer a matriz fazendo o SOMATÓRIO dos elementos em seguida será verificado se a soma
    é menor que o valor minimo armazendo, se for ele é atualizado. 
    '''
    for j in range(M):
        soma = 0
        for i in range(N):
            soma = soma + matrizA[i][j]
        if soma < minimo:
            minimo = soma

    '''
    for para fazer o produto, mesma logica do somatório.
    '''
    for j in range(N):
        produto = 1
        for i in range(M):
            produto = produto * matrizA[j][i]
        if produto > maximo:
            maximo = produto

    '''
    Eu tenho certeza que poderia jogar o retorno diretamente, mas simplesmente não funcionou
    acabei colocando a variavel resultado com um condicional e isso ta ferindo meu ego.... 
    '''
    print(minimo)
    print(maximo)
    resultado = 0
    if minimo <= maximo:
        resultado = 1
    return resultado

def main():
    global matrizA
    gerarmatriz()
    condicao = verificar()
    if condicao == 1:
        print("Condição Satisfeita")
    else:
        print("Condição não Satisfeita")


main()
