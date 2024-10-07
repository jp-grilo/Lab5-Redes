import socket
import os

# Definir endereço e porta do servidor
HOST, PORT = '', 8080

# Criar um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o socket ao endereço e porta definidos
server_socket.bind((HOST, PORT))

# Colocar o socket em modo de escuta
server_socket.listen(1)
print(f'Servidor rodando em http://{HOST}:{PORT}')

while True:
    # Aceitar uma conexão de um cliente
    client_connection, client_address = server_socket.accept()
    print(f'Conexão de {client_address}')

    # Receber a requisição HTTP do cliente
    request = client_connection.recv(1024).decode()
    print(f'Requisição recebida:\n{request}')

    # Analisar a requisição para determinar o arquivo requisitado
    request_line = request.splitlines()[0]
    filename = request_line.split()[1].lstrip('/')

    # Definir o nome do arquivo padrão se nenhum arquivo for requisitado
    if filename == '':
        filename = 'index.html'

    # Verificar se o arquivo requisitado existe
    if os.path.isfile(filename):
        # Ler o conteúdo do arquivo
        with open(filename, 'rb') as file:
            content = file.read()
        # Criar uma resposta HTTP com código 200
        response = b'HTTP/1.1 200 OK\r\n'
        response += b'Content-Type: text/html\r\n'
        response += b'Content-Length: ' + str(len(content)).encode() + b'\r\n'
        response += b'\r\n'
        response += content
    else:
        # Criar uma resposta HTTP com código 404
        response = b'HTTP/1.1 404 Not Found\r\n'
        response += b'Content-Type: text/html\r\n'
        response += b'\r\n'
        response += b'<html><body><h1>404 Not Found</h1></body></html>'

    # Enviar a resposta HTTP ao cliente
    client_connection.sendall(response)

    # Fechar a conexão
    client_connection.close()