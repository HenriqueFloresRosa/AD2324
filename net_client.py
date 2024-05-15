"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""


import pickle, struct
from sock_utils import *

class NetClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = create_tcp_client_socket(self.host, self.port)
        

    def connect(self):
        try:
            self.sock.connect((self.host, int(self.port)))
        except ConnectionAbortedError:
            print('error')
        except Exception as e:
            print(f"Error connecting to Server: {e}")
    
        

    def recebe(self):
        try:
            self.socket.settimeout(5)
            sizeByter = receive_all(self.socket, 4)
            size = struct.unpack('i', sizeByter)[0]


            Amsgbytes = receive_all(self.socket, size)
            report = pickle.loads(Amsgbytes)

            return report
        except Exception as e:
            self.socket.settimeout(None)
            print(f"Nao recebou dados: ERRO")

    def envia(self,data):
        try:
            msgBytes = pickle.dumps(data, -1)
            sizeByter = struct.pack('i', len(msgBytes))
            self.socket.sendall(sizeByter)
            self.socket.sendall(msgBytes)

        except Exception as e:
            print(f"Nao enviou dados: ERRO")

    def fechar(self):

        if self.socket:
            try:
                self.socket.close()
            except Exception as e:
                print(f"Erro a fechar a conexão: {e}")

    def __del__(self):
        
        try:
            self.socket.close()

        except Exception as e:
            print(f"Erro a fechar o socket do cliente:", e)