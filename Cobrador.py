from DBManager import *


class Cobrador(object):
    def __init__(self, nome, turno, senha, cpf):
        self.nome = nome
        self.turno = turno
        self.senha = senha
        self.cpf = cpf

    def Cadastrar_Cobrador(self,):
        banco = DBManager()
        banco.criar_tabela()
        banco.popular_tabela(self.nome, self.turno, self.senha, self.cpf)

    def Consulta_cobrador(self,):
        banco = DBManager()
        banco.consulta_tabela()