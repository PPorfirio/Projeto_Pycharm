import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")

host = "localhost"
port = 5432

s.bind((host, port))
mensagem = "servidor: oláaaaaa cliente e ae estão em pé!!"

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print("servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)
