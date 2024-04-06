"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Grupo: 14
Números de aluno: 56699 58618
"""

import sock_utils as su
import socket as s

class NetServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.conn_sock = None

    def accept_connection(self):
        try:
            self.conn_sock, (addr, port) = self.sock.accept()
            print(f"Accepted connection from {addr}:{port}")
        except s.error as e:
            print(f"Error accepting connection: {e}")

    def receive_message_from_stub(self):
        try:
            data = self.conn_sock.recv(1024)
            print(f"RECV from Stub: {data.decode()}")
            return data.decode()
        except s.error as e:
            print(f"Error receiving message from Stub: {e}")
            return None

    def send_response_to_stub(self, response):
        try:
            self.conn_sock.sendall(response.encode())
            print(f"SENT to Stub: {response}")
        except s.error as e:
            print(f"Error sending response to Stub: {e}")

    def close_connection(self):
        if self.conn_sock:
            self.conn_sock.close()
        self.sock.close()

    def __del__(self):
        self.close_connection()
