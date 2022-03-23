#exercicio com carrinhos para trabalhar o processamento thread em paralelo.
import time
from threading import Thread
import time

def carro (velocidade, piloto):
    trajeto = 0
    while trajeto <= 10:
        trajeto+=velocidade
        time.sleep(0.5)
        print(f"Piloto: {piloto} Km: {trajeto} \n ")


t_carro_1 = Thread(target=carro, args=[1, 'Felipe Massa ``òº=o>'])
t_carro_2 = Thread(target=carro, args=[1.5,'Rubinho B ``òº=o>'])

t_carro_1.start()
t_carro_2.start()

