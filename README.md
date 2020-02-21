# TP3-Desenvolvimento-Python-para-Redes-e-Sistemas-Operacionais

8. Crie um programa cliente que:

    1. Conecte-se a um servidor via UDP de mesmo IP e porta 9991.
    
    2. Peça ao servidor que envie a quantidade total e disponível de armazenamento do disco principal.
    
    3. Receba e exiba a informação.

9. Associado à questão anterior, crie um programa servidor que:

    1. Espere conexões UDP de processos na porta 9991.
    
    2. Aguarde indefinidamente conexão de clientes.
    
    3. Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal (diretório corrente que o processo servidor está executando).

10. Crie um programa cliente que:

    1. Conecte-se a um servidor via TCP de mesmo IP e porta 8881.
    
    2. Envie ao servidor o nome de um arquivo para que ele transmita este arquivo para o cliente.
    
    3. Receba o tamanho do arquivo.
    
    4. Se o tamanho for válido, receba o arquivo. Caso contrário, avise ao usuário que o arquivo não foi encontrado.

11. Associado à questão anterior, crie um programa servidor que:

    1. Espere conexões TCP de processos na porta 8881.
    
    2. Aguarde indefinidamente conexão de clientes.
    
    3. Receba a requisição do arquivo do cliente e envie o seu tamanho, caso o tenha encontrado. Em caso negativo, envie um valor inválido -1.
    Envie o arquivo para o cliente, caso o encontre.
