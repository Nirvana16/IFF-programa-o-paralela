'''
7) Considere um vetor com 20 números naturais maiores do que 1 lidos pelo
teclado. Faça um algoritmo recursivo que organize esse vetor de modo que os
números compostos fiquem nas primeiras posições e os números que não são
compostos nas últimas posições. Essa organização deve ser realizada sem utilizar
qualquer estrutura de dados auxiliar.
Crie e utilize dois procedimentos: um para preencher o vetor e outro
recursivo para realizar a organização do vetor. Crie e utilize também uma função
para retornar 1, se um número natural for composto, ou retornar 0, caso contrário.
Obs. 1: Um número natural C é composto se ele tem mais de dois divisores
naturais distintos.
Obs. 2: Não é permitido utilizar qualquer outro vetor/matriz para auxiliar a
ordenação.
'''
from random import randrange

N = 20
'''
Procedure de apoio, apenas para debug
'''
def teste():
    global vetor
    #vetor = [103, 3, 5, 7, 11, 13, 17, 19, 23, 29, 30, 36, 42, 44, 46, 54, 58, 60, 68, 72]
    vetor = [randrange(1, 199) for i in range(N)]
    print(vetor)

'''
Nada de novo aqui
'''
def preencher():
    global vetor
    vetor=[]
    for n in range(N):
        vetor.append(int(input("digite o numero: ")))


'''
Função que recebe um numero e retorna 1 ou 0 caso seja um numero composto ou primo
'''
def checanumero(numero):
    denominador = 1
    divisores = 0
    if numero > 3:
        for j in range(numero):
            if numero % denominador == 0:
                divisores += 1
            denominador += 1
        if divisores > 2:
            return 1
        else:
            return 0
    else:
        return 0

'''
procedure de organização do vetor. 
'''
def organizar(n):
    global vetor, apoio
    if n >= 0:
        for i in range(len(vetor)):
            if checanumero(vetor[i]) == 1:
                aux = vetor[i]
                del vetor[i]
                vetor.insert(0, aux)
        organizar(n-1)


def main():
    global vetor
    #preencher()
    teste()
    organizar(N-1)
    print(vetor)
    #print(checanumero(68))
main()