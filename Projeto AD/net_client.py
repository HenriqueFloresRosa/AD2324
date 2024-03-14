"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""
import socket
from sock_utils import *

class NetClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
            return print('conectado')
        except socket.error as e:
            print(f"Error connecting to {self.host}:{self.port}: {e}")
            return False

    def recv(self):
        try:
            data = self.sock.recv(1024)
            print(f'data receive: ')
            return data.decode()
        except socket.error as e:
            print(f"Error receiving data: {e}")
            return None

    def send(self, data):
        try:
            self.sock.sendall(data.encode())
            print(f'data receive: ')
            return True
        except socket.error as e:
            print(f"Error sending data: {e}")
            return False

    def close(self):
        self.sock.close()

    def __del__(self):
        self.close()
