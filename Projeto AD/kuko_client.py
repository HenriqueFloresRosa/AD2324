"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 14
Números de aluno: 56699 58618
"""
import sys
import socket
from kuko_data import *
from net_client import *

class KukoClient:
    def __init__(self, participant_id, server_host, server_port):
        self.participant_id = participant_id
        self.server_host = server_host
        self.server_port = server_port
        self.sock = None

    def connect_to_server(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.server_host, self.server_port))
            print("Connected to the server.")
        except Exception as e:
            print("Error:", e)
            sys.exit(1)

    def send_command(self, command):
        try:
            self.sock.sendall(command.encode())
            response = self.sock.recv(1024).decode()
            return response
        except Exception as e:
            print("Error:", e)
            sys.exit(1)

    def close_connection(self):
        try:
            self.sock.close()
            print("Connection closed.")
        except Exception as e:
            print("Error:", e)

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 kuko_client.py <participant_id> <server_host> <server_port>")
        sys.exit(1)

    participant_id = sys.argv[1]
    server_host = sys.argv[2]
    server_port = int(sys.argv[3])

    client = KukoClient(participant_id, server_host, server_port)
    client.connect_to_server()

    try:
        while True:
            command = input("comando > ")
            if command == "EXIT":
                client.close_connection()
                break
            else:
                response = client.send_command(command)
                print("Server response:", "OK")
    except KeyboardInterrupt:
        client.close_connection()
        print("Client program terminated.")

if __name__ == "__main__":
    main()


