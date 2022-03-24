# código para descobrir alguns dados de telefone usando a biblioteca phonenumbers, antes instale o pacote pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier  # descobrir a localização estadual

telefone = input(" Digite o numero do telefone fixo ou celular: ") # receber o número do telefone
num_tel = phonenumbers.parse(telefone, 'BR') #aqui colocando BR dispensamos a necessidade do +55
num_valido = phonenumbers.is_valid_number(num_tel) #validando a existencia do numero.
operadora = carrier.name_for_number(num_tel,'pt-br')
if num_valido == True:
    print(telefone)
    print(geocoder.description_for_number(num_tel,'pt'))
    print(operadora)
    print(num_valido)
else:
    print('/_\ Você digitou um numero que não existe, tente novamente')

