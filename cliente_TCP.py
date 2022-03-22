import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f"erro: {e}")
    print("Socket criado com sucesso")

    HostALvo = input ("Digite o host ou ip a ser conectado: ")
    PortalAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostALvo, int(PortalAlvo)))
        print("Cliente TCP conect com sucesso no host: " + HostALvo + "e na porta: " + PortalAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel conectar no host: " + HostALvo + " - Porta: " + PortalAlvo)
        print(f"Erro: {e}")
        sys.exit()
if __name__ == "__main__":
    main()

