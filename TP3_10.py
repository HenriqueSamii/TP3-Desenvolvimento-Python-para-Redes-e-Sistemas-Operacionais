"""10.Crie um programa cliente que:

    conecte-se a um servidor via TCP de mesmo IP e porta 8881.
    Envie ao servidor o nome de um arquivo para que ele transmita este arquivo para o cliente.
    Receba o tamanho do arquivo.
    Se o tamanho for válido, receba o arquivo. Caso contrário, avise ao usuário que o arquivo não foi encontrado."""

import os,socket,time
#tratamento de exeção dois lados, visualisador de download(percentagem com total no lado)

class arquivo_nao_existente(Exception):
    pass

download_dir = os.path.expanduser('~')+'\\Downloads\\'
socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
nome_arquivo = input('Digite o nome do arquivo: ')

try:
    socket_cliente.connect((socket.gethostname(),8881))
    socket_cliente.send(nome_arquivo.encode('ascii'))
    mensagem = socket_cliente.recv(12)
    tamanho = int(mensagem.decode('ascii'))
    if tamanho < 0:
        raise arquivo_nao_existente
    else:
        arquivo = open(download_dir + nome_arquivo, 'wb')
        soma = 0
        bytes = socket_cliente.recv(4096)
        while bytes:
            arquivo.write(bytes)
            soma = soma + len(bytes)
            print(soma,'de',tamanho)
            bytes = socket_cliente.recv(4096)
        arquivo.close()
except arquivo_nao_existente:
    print("Data menor que Zero")
except Exception as error:
    print(str(error))
socket_cliente.close()
input('Enter para sair')
