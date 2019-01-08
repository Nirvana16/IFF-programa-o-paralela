'''
Considere o arquivo “Numeros.txt” com 30 números inteiros. Faça um algoritmo
para armazenar esses números em um vetor e depois ordenar este mesmo vetor de
maneira não-decrescente. Utilize três procedimentos: um para preencher o vetor,
outro para ordenar o vetor e um terceiro para imprimir o vetor antes e depois da
ordenação.
Obs.: Não é permitido utilizar qualquer outro vetor/matriz para auxiliar a
ordenação.
'''

from random import randrange

N = 30

def preencher():
    global numeros
    arquivo = open("Numeros.txt", 'w')
    numeros = [randrange(1, 31) for i in range(N)]
    arquivo.write(str(numeros))
    arquivo.close()
    print("Numeros gerados no arquivo txt")


'''
O ex03 ficou com a parte de abertura do arquivo separar em uma procedure própria. Aqui deixei junto. 
Como já falei com mais detalhes como funciona a parte de leitura e preenchimento do vetor nas outras 
questões focarei apenas na lógica da ordenação

Utilizei dois For para que seja posivel comparar o elemento na posição vetor[i] com o vetor[j] se for maior
ele faz a perumuta. 
'''
def ordenar():
    global vetor
    arquivo = open("Numeros.txt", 'r')
    arquivo = arquivo.read()
    arquivo = arquivo.replace("[", "")
    arquivo = arquivo.replace("]", "")
    vetor = arquivo.split(",")
    for i in range(N):
        vetor[i] = int(vetor[i])

    #Como eu faria se estivesse trabalhando e precisasse organizar o vetor
    #vetor = sorted(vetor, key=int)

    #Como eu faço quando o professor pede na faculdade:
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]


def imprimir(vetorAntes, vetorDepois):
    print("Antes>>>")
    print(vetorAntes)
    print("Depois>>>")
    print(vetorDepois)

def main():
    global numeros, vetor
    preencher()
    ordenar()
    imprimir(numeros, vetor)


main()


