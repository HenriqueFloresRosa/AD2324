

"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Grupo: 14
Números de aluno: 56699 58618
"""
import socket as s

def create_tcp_server_socket(address, port, queue_size= 1):


    HOST = address
    PORT = int(port)

    try:
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(queue_size)
    except Exception as e:
        print("Erro ao criar o socket do servidor")
        exit(1)

    return sock


def create_tcp_client_socket(address, port):

    HOST = address
    PORT = int(port)

    try:
        sock =s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.connect((HOST, PORT))

    except Exception as e:
        print("Erro ao criar o socket ou a concetar ao servidor")
        exit(1)

    return sock


def receive_all(socket, length):
    dados_recebidos=b''
    while len(dados_recebidos) != length:
        socket.settimeout(5)
        try:
            dados_recebidos += socket.recv(length)

        except s.timeout as st:
            socket.settimeout(None)
            print("Sem dados")
            
    return dados_recebidos




    

