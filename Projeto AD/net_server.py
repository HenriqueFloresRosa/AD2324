"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Grupo: 14
Números de aluno: 56699 XXXXX
"""
import socket
from sock_utils import *

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_sock = None

    def accept(self):
        try:
            self.conn_sock, (addr, port) = self.sock.accept()
            print(f"Connected to {addr} on port {port}")
            return True
        except socket.error as e:
            print(f"Error accepting connection: {e}")
            return False

    def listen(self):
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            return True
        except socket.error as e:
            print(f"Error listening on {self.host}:{self.port}: {e}")
            return False

    def recv(self):
        try:
            data = self.conn_sock.recv(1024)
            return data.decode()
        except socket.error as e:
            print(f"Error receiving data: {e}")
            return None

    def send(self, texto):
        try:
            self.conn_sock.sendall(texto.encode())
            return True
        except socket.error as e:
            print(f"Error sending data: {e}")
            return False

    def close(self):
        if self.conn_sock:
            self.conn_sock.close()
        self.sock.close()

    def __del__(self):
        self.close()



