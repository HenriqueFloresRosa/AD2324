"""
Aplicações Distribuídas - Projeto 1 - net_server.py
Grupo: 14
Números de aluno: 56699 58618
"""
import builds.sock_utils as socket_utils

class NetServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.conn_sock = None

    def accept_connection(self):
        try:
            self.sock = socket_utils.create_tcp_server_socket(self.host, self.port, 1)
            self.conn_sock, (addr, port) = self.sock.accept()
            print(f"Accepted connection from {addr}:{port}")
        except Exception as e:
            print(f"Error accepting connection: {e}")

    def receive_message_from_client(self):
        try:
            data = self.conn_sock.recv(1024)
            print(f"RECV from Client: {data.decode()}")
            return data.decode()
        except Exception as e:
            print(f"Error receiving message from Client: {e}")
            return None

    def send_response_to_client(self, response):
        try:
            self.conn_sock.sendall(response.encode())
            print(f"SENT to Client: {response}")
        except Exception as e:
            print(f"Error sending response to Client: {e}")

    def close_connection(self):
        if self.conn_sock:
            self.conn_sock.close()
        if self.sock:
            self.sock.close()

    def __del__(self):
        self.close_connection()

