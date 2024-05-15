"""
Aplicações Distribuídas - Projeto 1 - net_client.py
Grupo: 14
Números de aluno: 56699 58618
"""
import sys
from kuko_stub import *
from kuko_data import *

class skeServer:

    def __init__(self):
        self.Kukodata = KUKO()

    def processMessage(self, pedidolist):
        cpo = pedidolist[0]
        id_participant = int()
