# GRUPO: Marcos, Jose Danilo, Sebastiao

'''
Para imprimir a cor usei a biblioteca termcolor com o COLORED
'''
from termcolor import colored
import threading
import time
from random import randrange

'''
A seguir é definido as 3 Threads, uma para cada cor. cada Thread recebe como parametro a quantidade vezes que ela será
executada por mei do paramentro "n" o controle de concorrencia "lock" e o tempo que ela irá adormecer. 

Quando a thread inicia ela trava a região critica utilizado o metodo acquire() do lock 
Em seguida inicia sua execução de printar a cor correspondente por N vezes, para impressão em cores basta utilizar 
o "colored" antes da string a ser impressa e em seguida passar a cor do texto sendo facultativo definir a cor de fundo 
e atributos tais como negrito ou italico. 

Realizada a impressão a Thread avisa que irá dormir pelo tempo recebido no parametro, essa espera é realizada por meio
do time.sleep. Em seguida ela libera a controle de concorrencia utilizando o metodo realease, assim a proxima thread
fica autorizada a entrar na região critica.
'''


def threadRed(n, lock, tempo):
    lock.acquire()
    for i in range(n):
        print(colored("vermelho", 'grey', 'on_red', attrs=['dark', 'bold']))
    print(colored("Vou dormir por %d, um abraço!" % tempo, 'red'))
    time.sleep(tempo)
    lock.release()


def threadYellow(n, lock, tempo):
    lock.acquire()
    for i in range(n):
        print(colored("Amarelo", 'grey', 'on_yellow', attrs=['dark', 'bold']))
    print(colored("Vou dormir por %d, um abraço!" % tempo, 'yellow'))
    time.sleep(tempo)
    lock.release()


def threadGreen(n, lock, tempo):
    lock.acquire()
    for i in range(n):
        print(colored("Verde", 'grey', 'on_green', attrs=['dark', 'bold']))
    print(colored("Vou dormir por %d, um abraço!" % tempo, 'green'))
    time.sleep(tempo)
    lock.release()

'''
o controle de concorrencia eh realizado por meio do threading.Lock() nativo do próprio python, ficando a cargo da 
biblioteca controlar a execução em mais baixo nivel, a fila de execução é feita de acordo com a chamada das Threads, ou seja
a primeira a ser chamada é a primeira da fila , a segunda Thread é a segunda da fila e assim sucessivamente..

o conceito das variaveis repetições, tempo e da atribuição e inicio das threads é a mesma do trabalho T2. o que muda aqui
é que fiz de modo menos elegante (sem usar um for para iniciar as threads) e precisei usar o .join() em cada Thread inciada
para incluir a mesma na fila de execução, o join diz que a Thread em questão tem sua execução em conjunta, ou dependente, 
de outras previamente ou posteriormente incluidas no lote. 
 
'''
lock = threading.Lock()
repeticoes = randrange(1, 21)
tempo = randrange(1, 11)
t_red = threading.Thread(target=threadRed, args=(repeticoes, lock, tempo))
repeticoes = randrange(1, 21)
tempo = randrange(1, 11)
t_yellow = threading.Thread(target=threadYellow, args=(repeticoes, lock, tempo))
repeticoes = randrange(1, 21)
tempo = randrange(1, 11)
t_green = threading.Thread(target=threadGreen, args=(repeticoes, lock, tempo))
t_red.start()
t_yellow.start()
t_green.start()
t_red.join()
t_yellow.join()
t_green.join()
