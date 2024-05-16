"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Grupo: 14
Números de aluno: 56699 58618
"""
import socket as s

def create_tcp_server_socket(address, port, queue_size):

    listener_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    listener_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    listener_socket.bind((address, port))
    listener_socket.listen(queue_size)
    return listener_socket


def create_tcp_client_socket(address, port):

    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    client_socket.connect((address, port))
    return client_socket


def receive_all(socket, length):
    dados_recebidos=b''

    while len(dados_recebidos) < length:
        dados_recebidos += socket.recv(length - len(dados_recebidos))
    return dados_recebidos
   
