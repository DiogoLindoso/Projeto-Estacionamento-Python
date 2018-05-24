#from Cobrador import *
from DBManager import *
from Login import *
#from EntradaVeiculo import *
#from GUI_Cobrador import *
#banco = DBManager()
#banco.consulta_tabela_veiculo()
#banco.consulta_tabela()
login = Login()

"""

print("Olá seja bem vindo ao sistema de estacionamento!")
cadastrar = input("Deseja cadastrar um novo cobrador? s / n").lower()
"""
"""if (cadastrar == "s"):
    nome = input("Informe seu nome!")
    turno = input("informe seu turno!")
    senha = input("informe sua senha")
    cpf = input("informe seu cpf")
    novo_cobrador = Cobrador(nome, turno, senha, cpf)
    novo_cobrador.Cadastrar_Cobrador()
else:
    pass
    #nomecompara = input("informe seu nome")
    #senhacompara =input("informe sua senha")
"""


#veiculo_entrada = Veiculo()
#print(type(veiculo_entrada))
#veiculo_entrada.set_placa()
#veiculo_entrada.set_registrar_entrada()
#veiculo_entrada.tempo_permanencia()
banco = DBManager()
#banco.criar_tabela()
#banco.consulta_tabela()
banco.close()
