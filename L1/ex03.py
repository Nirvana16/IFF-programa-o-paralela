'''
Considere um vetor que armazena 10 números inteiros pares e 10 números
inteiros ímpares todos embaralhados, ou seja, sem qualquer ordem preestabelecida.
Faça um algoritmo para ler esse vetor do arquivo “Vetor.txt” e depois organizá-lo
de modo que os números pares fiquem nas posições ímpares do vetor e os
números ímpares fiquem nas posições pares do vetor. Crie dois procedimentos:
um para preencher o vetor com os números do arquivo e o outro para organizá-lo.
'''
from random import randrange

N = 10


'''
A Procedure preencherVetor abre um arquivo TXT na raiz do programa.
o vetor 'numeros' de tamanho 90 recebe uma lista aleatória que em seguida sera gravada no arquivo.

A geração do vetor estava aleatória, contudo percebi que dos 10 elementos do vetor não haveria, necessáriamente, 
5 pares e 5 impares, então  vi que a questão não fala nada sobre gerar aleatóriamente ai fiz o vetor estatico mesmo
'''
def preencherVetor():
    arquivo = open("Vetor.txt", 'w')
    #numeros = [randrange(1, 91)for i in range(N)]
    numeros = [17, 27, 37, 47, 57, 10, 20, 30, 40, 50]
    arquivo.write(str(numeros))
    arquivo.close()

    print("Numeros gerados no arquivo txt")


'''
Essa procedure não era obrigatória, a questão pede apenas 3. Eu iria colocar a parte de leitura do 
arquivo dentro da procedure para organizara o vetor mas iria ficar bagunçado e com elementos que não 
tinham nada a ver com a procedure de organização então optei por gerar uma nova.

Ela gera um vetor de 10 posições com elementos zero. em seguida abre o arquito txt e faz as alterações
necessárias para transformar o formato string do mesmo em um int que pode ser lido e manipulado.
'''
def lerVetor():
    vetor = [0 for i in range(N)]
    arquivo = open("Vetor.txt", 'r')
    arquivo = arquivo.read()
    arquivo = arquivo.replace("[", "")
    arquivo = arquivo.replace("]", "")
    arquivo = arquivo.split(",")
    for i in range(N):
        vetor[i] = int(arquivo[i])
    return vetor

'''
procedure organizar.
Esse procedimento é bem simples, a lógica fica na parte condicional. Assim que o for começa a 
varrer o vetor da variavel global, quando o For varre o vetor ele vai checando se o resto da divisão inteira de cada elemento é 
zero ou não, se for par sempre será zero. Quando o resto for diferente de zero o elemento em questão é movido para o inicio
do vetor, (copiando ele e depois deletando a posição original) de forma a por todos os impares no começo do vetor.

Uma vez que os impares estejam organizados um novo for varre o vetor novamente, dessa vez só vamos nas posições
impares, por isso ele começa em "1" , vai até N-2, (no caso 8), indo de duas em duas casas com isso ele inserre no 
vetor os elementos que estiverem na posição correspondente a parte inteira de N+1, 1 , 3 , 5 e 7. sendo 20  30
40 e 50. por fim deletando todos os elementos do vetor que estiverem na posicao 8 em diante. (N:)

'''
def organizar():
    global vetor
    for i in range(N):
        if vetor[i] % 2 != 0:
            vetor.insert(0, vetor[i])
            del vetor[i + 1]
    for i in range(1, N-2, 2):
        vetor.insert(i, vetor[i + N//2])
    del vetor[N:]

def main():
    global vetor
    preencherVetor()
    vetor = lerVetor()
    print("Vetor Fora de ordem")
    print(vetor)
    organizar()
    print("Vetor Organizado")
    print(vetor)
main()
