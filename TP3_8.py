"""8.Crie um programa cliente que:

    conecte-se a um servidor via UDP de mesmo IP e porta 9991.
    Peça ao servidor que envie a quantidade total e disponível de armazenamento do disco principal.
    Receba e exiba a informação."""
import socket
#porta IP servidor - Enviar
host = socket.gethostname()
port = 9991
socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (host,port)

while True:
    mesagem = input('Degite "d" para receber quantidade total e disponível de armazenamento do disco principal')
    socket_server.sendto(mesagem.encode('ascii'),dest)
    if mesagem == 'sair':
        break
    else:
        ack_mensagem,address = socket_server.recvfrom(1024)
        print(ack_mensagem.decode('ascii'))

socket_server.close()