
"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""


from net_client import *

class KukoStub:

    
    def __init__(self, host, port):
        self.conn_sock = None
        self.port = port
        self.host = host
        self.conexão = NetClient(self.host, self.port)

    def connect_server(self):
        return self.conexão.connect()
    
    def enviar_lists(self, data):
        return self.conexão.recebe(data)

    def receber_lists(self):
        return self.conexão.envia()
    
    def close(self):
        return self.conexão.fechar()

