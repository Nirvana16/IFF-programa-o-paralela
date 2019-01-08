'''
Considere uma matriz M de ordem 3 de números inteiros armazenada no arquivo
“MatrizM.txt”. Faça um algoritmo para ler esta matriz do arquivo e imprimir na
tela se ela é ou não uma Matriz Ortogonal
Utilize três procedimentos: um para gerar a matriz M, outro para calcular a
sua matriz Transposta (MT) e o terceiro para calcular a multiplicação M.MT.
Utilize também uma função para retornar se a matriz M é Ortogonal ou não. A
impressão dessa informação tem que ser na função main.
Obs.: Se uma matriz quadrada M é uma matriz ortogonal, então M.MT = I,
onde MT é a matriz transposta de M e I a matriz identidade.
'''

from random import randrange

'''
Necessário para controle da procedure transpor
'''
N, M = 3, 3

'''
Procedimento para geração da matriz M
'''
def gerarmatriz():
    global matrizM
    arquivo = open("MatrizM.txt", 'w')
    matrizM = [[randrange(1, 99) for j in range(M)] for i in range(N)]
    arquivo.write(str(matrizM))
    arquivo.close()
    print("Gerando Matriz")
    for x in matrizM:
        print(*x, sep=" ")


'''
Procedimento para calcular a transposta
'''
def transpor():
    global transpostaM
    global matrizM
    transpostaM = [[0 for j in range(M)] for i in range(N)]
    '''
    Tenho que fazer a substituição com o Replace pois  o python salva a "matriz" como um array de arrays
    deste modo não daria para encontrar o elemento a[1][2](exemplo) pois ele acabaria considerando o espaço, virgula
    e [ como dados da matriz.  
    '''
    arquivo = open("MatrizM.txt", 'r')
    arquivo = arquivo.read()
    arquivo = arquivo.replace("[", "")
    arquivo = arquivo.replace("]", "")
    arquivo = arquivo.split(",")

    '''
    Para transpor a matriz criei dois FOR, de i a N e de J a M, de acordo com o tamanho da matriz do enunciado
    Eu preciso pegar cada elemento do nosso arquivo (array) e jogar na posição que eu quero da matriz. em seguida
    basta eu aplicar a regra da transporta e inverter essa posição.

    '''
    for i in range(N):
        for j in range(M):
            apoio = ((N * i) + j)
            matrizM[i][j] = int(arquivo[apoio])

    print("Transpondo a Matriz")
    for i in range(N):
        for j in range(M):
            transpostaM[i][j] = matrizM[j][i]

    for x in transpostaM:
        print(*x, sep=" ")


def verificar():
    '''
    Para verificação se a matriz é ortogonal basta ver se a diagonal sera composta de "1"
    '''

    global matrizM, transpostaM
    print("Verificando")
    for i in range(N):
        for k in range(M):
            soma = 0
            for j in range(M):
                soma = soma + matrizM[i][j] * transpostaM[j][k]
            # verifica se o elemento da matriz é o da diagonal
            if i == k:
                # se for um elemento da diagonal ele checa se o valor é diferente de 1
                if soma != 1:
                    return False
            elif soma != 0:
                return False
    return True


def main():
    gerarmatriz()
    transpor()
    if verificar():
        print("Matriz ortogonal")
    else:
        print("Matriz Não ortogonal")


main()
