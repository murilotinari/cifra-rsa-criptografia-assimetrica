## 📸 Evidências

Aqui estão algumas capturas de tela e exemplos de execução que demonstram o funcionamento do projeto:

- **🔐 Criptografia e Descriptografia**: Abaixo você pode ver como o cliente envia uma mensagem criptografada ao servidor, que a descriptografa corretamente.
  
 ![image](https://github.com/user-attachments/assets/59bd90f3-e93f-4191-8598-13ef360a51e7)

- **💻 Execução do Servidor**: Captura de tela do servidor em funcionamento, mostrando a geração das chaves RSA, a recepção da mensagem e a resposta do servidor enviada ao cliente após a descriptografia da mensagem.
  
  ![Comunicacao Server](https://github.com/user-attachments/assets/5ad8bc8a-13d4-4b46-a55a-15438e54384f)


- **📨 Rastreio Wireshark**: A comunicação TCP rastreada através da ferramenta Wireshark.

  ![image](https://github.com/user-attachments/assets/571adf07-b38c-4dac-a146-91e75fd8f9b6)


---

## 💻 Cliente

O código do cliente é responsável por:

- **🔑 Receber a chave pública do servidor** para criptografar a mensagem.
- **💬 Solicitar ao usuário uma mensagem** e criptografá-la utilizando a chave pública.
- **📤 Enviar a mensagem criptografada** ao servidor e aguardar uma resposta.
- **📨 Exibir a resposta** do servidor, que contém a mensagem descriptografada.



## 🖥️ Servidor

O código do servidor é responsável por:

- **🔒 Gerar as chaves RSA** (pública e privada) quando iniciado.
- **📬 Enviar a chave pública** para o cliente, permitindo que ele criptografe a mensagem.
- **📥 Receber a mensagem criptografada** do cliente e descriptografá-la usando a chave privada.
- **📨 Enviar uma resposta** ao cliente confirmando a recepção e a descriptografia da mensagem.


## 👥 Integrantes

Este projeto foi desenvolvido por:

- **👨‍💻 André Vitor Pereira Cini**: 
- **👩‍💻 Gustavo Peterlini de Oliveira**
- **👨‍💻 Lucas Leite Vaz de Lima**
- **👨‍💻 Murilo Tinari Abdalla**
