# um gerador de hash para frases.
import hashlib

string = input("Digite sua frase a ser gerado o hash: ")
menu = int( input(''' ### Escolha o TIPO de HASH para sua Frase ###
                  1) MD5 2) SHA1 3) SHA256 4) SHA 512
                  Digite o numero do HASH escolhido: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("O HASH MD5 da frase é: ", string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("O HASH SHA1 da frase é: ", string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("O HASH SHA256 da frase é: ", string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("O HASH SHA512 da frase é: ", string, 'é: ', resultado.hexdigest())

else:
    print("Algo deu errado refaça a operação")