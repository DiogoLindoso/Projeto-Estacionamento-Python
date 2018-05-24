from datetime import *
from DBManager import *


class Veiculo(object):

    def __init__(self):
        self.placa = ""
        self.data_hora_entrada = ""
        self.data_hora_pagamento = 0
        self.hora_limite_saida = 0
        self.banco = DBManager

    def set_placa(self, placa, data):

        self.placa = placa
        self.data_hora_entrada = data

        self.banco.inserir_veiculo(DBManager(), self.placa, self.data_hora_entrada)

    def tempo_permanencia(self):
        permanencia = datetime.now()-self.data_hora_entrada
        print("O tempo de permanencia foi de %s" % (str(permanencia)))
