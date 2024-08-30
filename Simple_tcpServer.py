from socket import *
from Crypto.Util import number
from Crypto import Random

# Define a porta do servidor
serverPort = 1300

# Criação do socket TCP do servidor
serverSocket = socket(AF_INET, SOCK_STREAM)

# Vincula o socket à porta especificada e ao endereço IP da máquina
serverSocket.bind(("", serverPort))

# Coloca o servidor em modo de escuta, permitindo até 5 conexões pendentes
serverSocket.listen(5)

print("TCP Server\n")

# Aceita uma conexão de um cliente (bloqueia até que um cliente se conecte)
connectionSocket, addr = serverSocket.accept()

# Gera as chaves RSA para criptografia
bitlen = 4096  # Define o tamanho dos bits para as chaves
r = Random.new().read
p = number.getPrime(bitlen // 2, r)  # Gera um número primo grande p
q = number.getPrime(bitlen // 2, r)  # Gera um número primo grande q
n = p * q  # Calcula n = p * q
m = (p - 1) * (q - 1)  # Calcula a função totiente phi(n) = (p - 1) * (q - 1)
e = number.getPrime(17)  # Escolhe um pequeno número primo para e
while number.GCD(e, m) != 1:  # Garante que e seja coprimo com m
    e += 2
d = number.inverse(e, m)  # Calcula o inverso modular de e para obter d

# Envia a chave pública (n, e) para o cliente
connectionSocket.send(f"{n},{e}".encode())
print(f"Chave N: {n}")
print(f"Chave E: {e}")

# Recebe a mensagem criptografada do cliente
msg_cifrada = int(connectionSocket.recv(4096).decode())

print(f"Mensagem cifrada: {msg_cifrada}")

# Descriptografa a mensagem usando a chave privada (d, n)
msg_decifrada = pow(msg_cifrada, d, n)
msg_decifrada = msg_decifrada.to_bytes((msg_decifrada.bit_length() + 7) // 8, 'big').decode()

print(f"Mensagem decifrada: {msg_decifrada}")

# Envia a mensagem descriptografada de volta ao cliente
connectionSocket.send(f"Mensagem recebida: {msg_decifrada}".encode())

# Fecha a conexão com o cliente
connectionSocket.close()

# Fecha o socket do servidor
serverSocket.close()
