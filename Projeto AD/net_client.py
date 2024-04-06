"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""

import socket
import pickle

class NetClient:
    def __init__(self, stub_host, stub_port):
        self.stub_host = stub_host
        self.stub_port = stub_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_stub(self):
        try:
            self.sock.connect((self.stub_host, self.stub_port))
            print("Connected to Stub.")
        except socket.error as e:
            print(f"Error connecting to Stub: {e}")

    def send_message_to_stub(self, message):
        try:
            self.sock.sendall(message.encode())
            print(f"SENT to Stub: {message}")
        except socket.error as e:
            print(f"Error sending message to Stub: {e}")

    def close_connection(self):
        self.sock.close()

    def __del__(self):
        self.close_connection()

class KukoClient:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port

    def send_request(self, request_code, *args):
        request = [request_code] + list(args)
        serialized_request = pickle.dumps(request)
        return self.send_to_server(serialized_request)

    def send_to_server(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.server_address, self.server_port))
                sock.sendall(data)
                serialized_response = sock.recv(4096)
                return pickle.loads(serialized_response)
            except socket.error as e:
                print(f"Error communicating with server: {e}")

