import socket as s
import sys
from kuko_data import KUKO
from kuko_ske import *

class KukoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.kuko = KUKO()  # Instância da classe KUKO para gerenciar perguntas e quizzes

    def start(self):
        try:
            server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
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
            
            # Receber o ID do participante
            participant_id = conn_socket.recv(1024).decode().strip()
            print(f"Participant ID: {participant_id}")

            # Responder juntamente com o endereço do cliente
            response = f"Connection from {conn_socket.getpeername()} Participant ID: {participant_id}"
            conn_socket.sendall(response.encode())

            self.handle_client(conn_socket, participant_id)
        except Exception as e:
            print("Error accepting connection:", e)

    def handle_client(self, conn_socket, participant_id):
        try:
            while True:
                request = conn_socket.recv(1024).decode().strip()
                if not request:
                    break

                response = self.process_request(request, participant_id)
                conn_socket.sendall(response.encode())
                print("RECV:", response)  # Resposta do servidor
        except Exception as e:
            print("Error handling client request:", e)
        finally:
            print("Closing connection with client.")
            conn_socket.close()


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


