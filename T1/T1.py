"""
Python ja possui um módulo nativo para threads, basta fazer a importação dele.
Também usei o Time para conseguir pausar a execução e ela não ficar muito rapida
"""
import threading
import time


"""
 A Função exibirMensagem recebe uma mensagem qualquer como parametro e exibe ela em um loop por 17 vezes.
"""
def exibirMensagem(message):
    for i in range(17):
        print(message)
        time.sleep(1)

"""
 É feito a criação de dois objetos, cada um chamando a mesma função anterior só que passando uma mensagem diferente.
 Para o Thread , em python, é preciso informar que estamos tratando de uma thread e também passar a função que sera trabalhada
 além dos argumentos da mesma, caso exista.
"""
t1 = threading.Thread(target=exibirMensagem, args=("1 - Programação Paralela",))
t1.start()
t2 = threading.Thread(target=exibirMensagem, args=("2 - Instituto Federal Fluminense",))
t2.start()

"""
Este while faz a emissao de uma mensagem enquanto as treads 1 e 2 estiverem ativas.
"""
while t1.isAlive() and t2.isAlive():
    print("\nAguardando thread\n")
    time.sleep(5)

print("Concluido")


"""
Nenhum tratamento de sincronismo foi efetuado, dessa forma as treads 1 e 2 podem ser executadas fora de ordem. 
"""