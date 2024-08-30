# Bibliotecas necessárias para o código:
import json
import os
import random
from socket import *
import sympy
import base64
from Crypto.Util import number


#######################
# Cifra RSA em Python #
#######################


##################################
# GRUPO                          #
# * Abrão Asterio Junior         #
# * Alexandre Bezerra de Andrade #
# * Daniel Santos de Sousa       #
# * Francisco Tommasi Silveira   #
##################################


#### FUNÇÕES AUXILIARES ####

####################################################
# Função para gerar um número primo grande
# Parâmetros:
#   bits: tamanho dos bits
# Retorno:
#   um número primo grande
def generate_large_prime(bits):
    return sympy.randprime(2**(bits-1), 2**bits)
####################################################



####################################################
# Função para calcular o GCD (Máximo Divisor Comum)
# Parâmetros:
#   a: número
#   b: número
# Retorno:
#   o MDC entre os dois números
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
####################################################



####################################################
# Função para calcular o inverso modular usando o algoritmo estendido de Euclides
# Parâmetros:
#   e: número
#   phi: número
# Retorno:
#   o inverso modular de 'e' em relação a 'phi'
def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi
####################################################



####################################################
# Função para gerar as chaves RSA
# Parâmetros:
#   bits: tamanho dos bits
# Retorno:
#   chave pública (e, n) e chave privada (d, n)
def generate_rsa_keys(bits):
    # Gerar dois números primos grandes
    p = number.getStrongPrime(bits // 2)
    q = number.getStrongPrime(bits // 2)

    # Calcular n = p * q
    n = p * q

    # Calcular a função totiente de Euler (phi) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # Escolher um valor 'e' tal que 1 < e < phi e gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calcular o inverso modular de 'e', ou seja, d
    d = mod_inverse(e, phi)

    # Chave pública (e, n) e chave privada (d, n)
    return ((e, n), (d, n))
####################################################



####################################################
# Função para criptografar uma mensagem
# Parâmetros:
#   public_key: chave pública (e, n)
#   message: mensagem a ser criptografada
# Retorno:
#   a mensagem criptografada em base64
def encrypt_rsa(public_key, message):
    e, n = public_key

    # Convertendo a mensagem para inteiro
    message_int = int.from_bytes(message.encode('utf-8'), byteorder='big')

    # Criptografar usando a fórmula: ciphertext = message^e % n
    ciphertext = pow(message_int, e, n)

    # Converter o número criptografado para bytes
    encrypted_bytes = ciphertext.to_bytes((ciphertext.bit_length() + 7) // 8, byteorder='big')

    # Codificar em base64 para uma representação segura em UTF-8
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

    # Retornar a mensagem criptografada em base64
    return encrypted_base64
####################################################


####################################################
# Função para descriptografar uma mensagem
# Parâmetros:
#   private_key: chave privada (d, n)
#   encrypted_base64: mensagem criptografada em base64
# Retorno:
#   a mensagem descriptografada
def decrypt_rsa(private_key, encrypted_base64):
    d, n = private_key
    # Decodificar a mensagem base64 para bytes
    encrypted_bytes = base64.b64decode(encrypted_base64.encode('utf-8'))

    # Converter os bytes de volta para um inteiro
    ciphertext = int.from_bytes(encrypted_bytes, byteorder='big')

    # Descriptografar usando a fórmula: message = ciphertext^d % n
    decrypted_message_int = pow(ciphertext, d, n)

    # Converter o inteiro de volta para string
    decrypted_message = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

    # Retornar a mensagem descriptografada em UTF-8
    return decrypted_message
####################################################


####################################################
# Função para gravar a chave em um arquivo
# Parâmetros:
#   chave: chave a ser gravada
def gravarChaveArquivo(chave):
    # Checa se o arquivo existe
    if os.path.exists('chaves.txt'):
        os.remove('chaves.txt')

    # Grava a chave no arquivo
    with open('chaves.txt', 'w') as f:
        f.write(chave)
####################################################



# Função principal

if __name__ == "__main__":
    # Configurações do Client (Alice)
    serverName = "10.1.70.15" # Server IP Address
    serverPort = 1300
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    # Gerar chaves RSA de 4096 bits
    bitsEncodind = 4096
    public_key, private_key = generate_rsa_keys(bitsEncodind)
    print(f"Chaves públicas (e, n):\n{public_key}\n")
    print(f"Chaves privadas (d, n):\n{private_key}\n")

    # HANDSHAKE - Chave pública (R) recebida do servidor (Bob)
    #rRecebido = json.loads(str(clientSocket.recv(65000),"utf-8")).get("R")
    #print(f"R Recebido: {rRecebido}")

    #### MENSAGEM ENVIADA ####
    # Mensagem a ser criptografada
    message = "The information security is of significant importance to ensure the privacy of communications"

    # Criptografar a mensagem
    encrypted_message_utf8 = encrypt_rsa(public_key, message)
    
    #Enviar a mensagem
    clientSocket.send(json.dumps(f"Mensagem:{encrypted_message_utf8},Key:{public_key}","utf-8"))
    print(f"Mensagem criptografada em UTF-8 (Base64):\n{encrypted_message_utf8}\n")

    #### MENSAGEM RECEBIDA ####
    # Recebe a mensagem aberta do servidor em caixa alta
    text = str(clientSocket.recv(65000),"utf-8")
    print ("Received from Make Upper Case Server: ", text)

    # Fecha a conexão
    clientSocket.close()