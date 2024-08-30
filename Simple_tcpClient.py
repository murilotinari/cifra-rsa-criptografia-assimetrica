from socket import *

# Definição do nome do servidor e da porta na qual o servidor está ouvindo
serverName = "10.1.70.40"
serverPort = 1300

# Criação de um socket TCP (protocolo de transmissão confiável)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Conexão ao servidor usando o endereço IP e a porta especificados
clientSocket.connect((serverName, serverPort))

# Recebe a chave pública (n, e) enviada pelo servidor
public_key = clientSocket.recv(4096).decode()

# Divide a chave pública recebida em seus componentes (n e e)
n, e = map(int, public_key.split(','))

# Solicita ao usuário que insira uma frase para ser criptografada e enviada
sentence = input("Input your sentence: ")

# Criptografa a mensagem digitada usando a chave pública recebida
msg_cifrada = pow(int.from_bytes(sentence.encode(), 'big'), e, n)

# Envia a mensagem criptografada ao servidor
clientSocket.send(str(msg_cifrada).encode())

# Recebe a resposta do servidor, que pode ser a mensagem descriptografada
response = clientSocket.recv(4096).decode()

# Exibe a resposta recebida do servidor
print(response)

# Fecha a conexão com o servidor
clientSocket.close()
