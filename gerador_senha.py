import random  # Este módulo implementa geradores de números pseudoaleatórios para várias distribuições.
import string

tamanho = 16  # quantidade de caracteres
chars = string.ascii_letters + string.digits + "Ç~+_)(&%$#@!=-*/|\;.,?:><{}^"
# na linha acima temos a condição de moldar como s erá  nossa senha, maíuscula, minuscula mais ou menos caracteres
rnd = random.SystemRandom()  # gerar numeros aleatórios pelo sistema
print(''.join(rnd.choice(chars) for i in range(tamanho)))
