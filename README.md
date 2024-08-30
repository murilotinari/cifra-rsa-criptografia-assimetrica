# cifra-rsa-criptografia-assimetrica

## 📸 Evidências

Aqui estão algumas capturas de tela e exemplos de execução que demonstram o funcionamento do projeto:

- **🔐 Criptografia e Descriptografia**: Abaixo você pode ver como o cliente envia uma mensagem criptografada ao servidor, que a descriptografa corretamente.
  
  ![Exemplo de Criptografia](path-to-your-image/encryption_example.png)

- **💻 Execução do Servidor**: Captura de tela do servidor em funcionamento, mostrando a geração das chaves RSA e a recepção da mensagem.
  
  ![Execução do Servidor](path-to-your-image/server_running.png)

- **📨 Resposta ao Cliente**: Exemplo de resposta do servidor enviada ao cliente após a descriptografia da mensagem.

  ![Resposta ao Cliente](path-to-your-image/client_response.png)

---

## 💻 Cliente

O código do cliente é responsável por:

- **🔑 Receber a chave pública do servidor** para criptografar a mensagem.
- **💬 Solicitar ao usuário uma mensagem** e criptografá-la utilizando a chave pública.
- **📤 Enviar a mensagem criptografada** ao servidor e aguardar uma resposta.
- **📨 Exibir a resposta** do servidor, que contém a mensagem descriptografada.

### 📝 Código do Cliente

```python
# Seu código do cliente aqui
```

---

## 🖥️ Servidor

O código do servidor é responsável por:

- **🔒 Gerar as chaves RSA** (pública e privada) quando iniciado.
- **📬 Enviar a chave pública** para o cliente, permitindo que ele criptografe a mensagem.
- **📥 Receber a mensagem criptografada** do cliente e descriptografá-la usando a chave privada.
- **📨 Enviar uma resposta** ao cliente confirmando a recepção e a descriptografia da mensagem.

### 📝 Código do Servidor

```python
# Seu código do servidor aqui
```

---

## 👥 Integrantes

Este projeto foi desenvolvido por:

- **👨‍💻 Nome do Integrante 1**: [GitHub](https://github.com/seuusuario1)
- **👩‍💻 Nome do Integrante 2**: [GitHub](https://github.com/seuusuario2)
- **👨‍💻 Nome do Integrante 3**: [GitHub](https://github.com/seuusuario3)
