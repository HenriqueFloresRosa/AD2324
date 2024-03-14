"""
Aplicações Distribuídas - Projeto 1 - kuko_server.py
Grupo: 14
Números de aluno: 56699 58618
"""

import socket
import sys
from kuko_data import Kuko

class KukoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.kuko = Kuko()

    def start(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print(f"Kuko server started on {self.host}:{self.port}")
            while True:
                self.accept_connection(server_socket)
        except KeyboardInterrupt:
            print("Server terminated by user.")
        finally:
            if server_socket:
                server_socket.close()

    def accept_connection(self, server_socket):
        try:
            conn_socket, (client_host, client_port) = server_socket.accept()
            print(f"Client connected from: {client_host} on port: {client_port}")
            self.handle_client(conn_socket)
        except Exception as e:
            print("Error accepting connection:", e)

    def handle_client(self, conn_socket):
        try:
            while True:
                request = conn_socket.recv(1024).decode().strip()
                if not request:
                    break
                print(f"Received request from client: {request}")
                # Process request and generate response
                response = self.process_request(request)
                conn_socket.sendall(response.encode())
        except Exception as e:
            print("Error handling client request:", e)
        finally:
            print("Closing connection with client.")
            conn_socket.close()

    def process_request(self, request):
    
        return "Server response to client request: " + request

def main():
    if len(sys.argv) != 3:
        print("Usage: python kuko_server.py <host> <port>")
        return
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    server = KukoServer(host, port)
    server.start()

if __name__ == "__main__":
    main()


