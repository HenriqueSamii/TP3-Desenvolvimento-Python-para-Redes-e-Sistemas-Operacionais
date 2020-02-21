"""9.Associado à questão anterior, crie um programa servidor que:

    Espere conexões UDP de processos na porta 9991.
    Aguarde indefinidamente conexão de clientes.
    Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal (diretório corrente que o processo servidor está executando)."""

import socket,psutil
#porta IP servidor -Receber
socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host_name = socket.gethostname()
socket_server.bind((host_name,9991))

print('Esperando receber na porta', 9991)

while True:

    pacote, destino = socket_server.recvfrom(1024)
    cliente_input = pacote.decode('utf-8')
    ack = 'ACK'.encode('ascii')
    
    if cliente_input == 'd':
        ack = str(psutil.disk_usage('/')).encode('ascii')
    elif cliente_input == 'sair':
        break
    else:
        ack = str('Opção',cliente_input,'não valida').encode('ascii')

    socket_server.sendto(ack,destino)

socket_server.close()
input('Coneção termoinada, pressione qualquer tecla para sair')