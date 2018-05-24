from sqlite3 import *
from datetime import *


class DBManager(object):

    def __init__(self):

        self.path = 'c:\sqlite\estacionamento_bd'
        self.conn = connect(self.path + '\estacionamento.db')
        self.c = self.conn

    def close(self):
        self.conn.close()

    def criar_tabela(self):
        # Criando Tabela de funcionarios
        self.c.execute('''CREATE TABLE IF NOT EXISTS funcionario
                            (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                turno TEXT NOT NULL,
                                senha TEXT NOT NULL,
                                cpf INT NOT NULL
                            )''')

        self.c.commit()

        #Criando tabela de Veiculos
        self.c.execute('''CREATE TABLE IF NOT EXISTS veiculo
                                    (
                                        placa TEXT NOT NULL,
                                        dia_hora_entrada TEXT NOT NULL,
                                        pago INT
                                                                                
                                    )''')

        self.c.commit()

    def popular_tabela(self, nome, turno, senha, cpf):
        t = [(nome, turno, senha, cpf)]
        self.c.execute("INSERT INTO funcionario (nome, turno, senha, cpf) VALUES (?,?,?,?)", t[0])
        self.c.commit()

    def inserir_veiculo(self, placa, entrada):
        pago = 0
        self.c.execute("INSERT INTO veiculo (placa, dia_hora_entrada, pago) VALUES (?,?,?)", (placa, entrada, pago))
        self.c.commit()

    def consulta_tabela(self):
        for row in self.c.execute('SELECT * FROM funcionario'):
            print(row)

    def consulta_tabela_veiculo(self):
        for row in self.c.execute('SELECT * FROM veiculo'):
            print(row)

    def valida_login(self, usuario, senha):
        n = 0
        for row in self.c.execute('SELECT nome, senha FROM funcionario WHERE nome=(?) AND senha=(?)', (usuario, senha)):
            print(row)
            n = n + 1
        if n == 1:
            print("Acesso Permitido")
            return True
        else:
            print("Acesso Negado")
            return False
