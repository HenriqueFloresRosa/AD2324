"""
Aplicações Distribuídas - Projeto 1 - kuko_server.py
Grupo: XX
Números de aluno: XXXXX XXXXX
"""

import sys
import socket as s
from net_server import *
from kuko_data import *

def main():
    HOST = "10.101.87.233"
    PORT = 5555
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn_sock, (adr, port) = sock.accept()
    print("Connected to %s on port %s" % (adr, port))
    msg = conn_sock.recv(1024)
    conn_sock.sendall("Resposta?".encode())
    sock.close()

if __name__ == "__main__":
    main()
