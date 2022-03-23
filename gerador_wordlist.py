'''É uma lista com conjuntos de senha de varios tipos possiveis,  que é usada normalmente
 em programas de brutforce (força bruta) para descobrir senhas de sistemas, emails, sites.'''

import itertools
string = input("Digite uma palavra aleatória: ")
resultado = itertools.permutations(string, len(string))
for i in resultado:
    print(''.join(i))