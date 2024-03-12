"""
Aplicações Distribuídas - Projeto 1 - sock_utils.py
Grupo: 14
Números de aluno: 56699 XXXXX
"""
import socket

def create_server_socket(host, port):
    """
    Criar um servidor socket e 
    """
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        return server_socket
    except socket.error as e:
        print(f"Error creating server socket: {e}")
        return None

def accept_connection(server_socket):
    """
    aceitar conexão entre sockets
    """
    try:
        conn_sock, (addr, port) = server_socket.accept()
        print(f"Connected to {addr} on port {port}")
        return conn_sock
    except socket.error as e:
        print(f"Error accepting connection: {e}")
        return None

def create_client_socket():
    """
    Criar um cliente (socket)
    """
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket
    except socket.error as e:
        print(f"Error creating client socket: {e}")
        return None

def connect_to_server(client_socket, host, port):
    """
    Connectar ao server o client, intermediário
    """
    try:
        client_socket.connect((host, port))
        return True
    except socket.error as e:
        print(f"Error connecting to {host}:{port}: {e}")
        return False

def receive_data(socket_obj):
    """
    Receber a data dos sockets
    """
    try:
        data = socket_obj.recv(1024)
        return data.decode()
    except socket.error as e:
        print(f"Error receiving data: {e}")
        return None

def send_data(socket_obj, data):
    """
    Enviar dat para os sockets 
    """
    try:
        socket_obj.sendall(data.encode())
        return True
    except socket.error as e:
        print(f"Error sending data: {e}")
        return False

def close_socket(socket_obj):
    """
    Fechar o socket
    """
    try:
        socket_obj.close()
    except socket.error as e:
        print(f"Error closing socket: {e}")

def shutdown_socket(socket_obj):
    """
    Finito socket (?)
    """
    try:
        socket_obj.shutdown(socket.SHUT_RDWR)
    except socket.error as e:
        print(f"Error shutting down socket: {e}")

    

