
"""
Python ja possui um módulo nativo para threads, basta fazer a importação dele.
Também usei o Time para conseguir pausar a execução e ela não ficar muito rapida
"""
import threading
import time
from random import randrange

"""
 Recebe a mensagem, o tempo e o numero da Thread.
 Printa a mensagem, seta o tempo que a Thread ira dormir e, após o termino do tempo,
 printa a mensagem de finalização 
"""
def exibirMensagem(message, tempo, thread_numero):
    print(message)
    time.sleep(tempo)
    print("Eu sou thread %d. Já se passaram %d segundos e serei finalizada!" % (thread_numero, tempo))

'''
    Cria-se a Threads, sendo que para cada uma é gerado uma variavel, "tempo", com valor aleatório de ate 20
    segundos. Em seguida chamo a função "threading.Thread" passando a função e os argumentos (menssagem, tempo e numero)
    logo após 
'''
for i in range(4):
    tempo = randrange(1, 21)
    t = threading.Thread(target=exibirMensagem, args=("Eu sou a Thread %d e vou dormir por %d segundos!" % (i, tempo), tempo, i))
    t.start()
