"""11.Associado à questão anterior, crie um programa servidor que:

    Espere conexões TCP de processos na porta 8881.
    Aguarde indefinidamente conexão de clientes.
    Receba a requisição do arquivo do cliente e envie o seu tamanho, caso o tenha encontrado. Em caso negativo, envie um valor inválido -1.
    Envie o arquivo para o cliente, caso o encontre."""

import socket,os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host,porta))
socket_servidor.listen()
print('Servidor de nome',host,"esperando na porta",porta)
while True:
    (socket_cliente, address) = socket_servidor.accept()
    print('conectado a:', str(address))
    mensagem = socket_cliente.recv(2048)
    nome_arquivo = mensagem.decode('ascii')
    if os.path.isfile(nome_arquivo):
        tamanho = os.stat(nome_arquivo).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        arquivo = open(nome_arquivo,'rb')
        bytesRead = arquivo.read(4096)
        while bytesRead:
            socket_cliente.send(bytesRead)
            bytesRead = arquivo.read(4096)
        arquivo.close()
    else:
        print('Arquivo não encontrado')
        socket_cliente.send('-1'.encode('ascii'))
    socket_cliente.close()
socket_servidor.close()
