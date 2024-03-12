"""
Aplicações Distribuídas - Projeto 1 - kuko_client.py
Grupo: 14
Números de aluno: 56699 XXXXX
"""

import sys
import socket as s
from net_client import *

import sys
import socket as s
from net_client import *

def main():
    HOST = "10.101.87.233"
    PORT = 5555
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall("Boas".encode())  # encode os bytes das strings
    resposta = sock.recv(1024)
    print(resposta.decode())  # resposta endcode
    sock.close()

if __name__ == "__main__":
    main()
