"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""
import builds.sock_utils as socket_utils

class NetClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.sock = None

    def connect_to_server(self):
        try:
            self.sock = socket_utils.create_tcp_client_socket(self.server_host, self.server_port)
            print("Connected to Server.")
        except Exception as e:
            print(f"Error connecting to Server: {e}")

    def send_message_to_server(self, message):
        try:
            self.sock.sendall(message.encode())
            print(f"SENT to Server: {message}")
        except Exception as e:
            print(f"Error sending message to Server: {e}")

    def close_connection(self):
        if self.sock:
            self.sock.close()

    def __del__(self):
        self.close_connection()
