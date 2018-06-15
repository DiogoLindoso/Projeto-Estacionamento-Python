from sqlite3 import *
from datetime import *


class DBManager(object):

    def __init__(self):

        self.path = 'c:\sqlite\estacionamento_bd'
        self.conn = connect(self.path + '\estacionamento.db')
        self.c = self.conn
        # Criando Tabela de funcionarios
        self.c.execute('''CREATE TABLE IF NOT EXISTS funcionario
                                    (
                                        id_funcionario INTEGER PRIMARY KEY,
                                        nome TEXT NOT NULL,
                                        turno TEXT NOT NULL,
                                        senha TEXT NOT NULL,
                                        cpf INT NOT NULL        
                                    )''')

        self.c.commit()

        # Criando tabela de Veiculos
        self.c.execute('''CREATE TABLE IF NOT EXISTS veiculo
                                            (   
                                                id_veiculo INTEGER PRIMARY KEY,
                                                tipo TEXT NOT NULL,
                                                placa TEXT NOT NULL,
                                                dia_hora_entrada TEXT NOT NULL,
                                                fk_id_funcionario_caixa,
                                                pago INT,
                                                FOREIGN KEY(fk_id_funcionario_caixa) REFERENCES funcionario(id_funcionario)
                                            )''')

        self.c.commit()

    def close(self):
        self.conn.close()
    """"
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
    """
    def popular_tabela(self, nome, turno, senha, cpf):
        self.c.execute("INSERT INTO funcionario (nome, turno, senha, cpf) VALUES (?,?,?,?)", (nome, turno, senha, cpf))
        self.c.commit()

    def inserir_veiculo(self, placa, entrada, tipo):
        pago = 0
        self.c.execute("INSERT INTO veiculo (placa, dia_hora_entrada, pago, tipo) VALUES (?,?,?,?)", (placa, entrada, pago, tipo))
        self.c.commit()

    def pagar(self, placa, tarifa, id_funcionario):
        self.c.execute("UPDATE veiculo SET pago=?, fk_id_funcionario_caixa =?  WHERE placa=?", (tarifa, id_funcionario, placa))
        self.c.commit()

    def consulta_tabela(self):
        for row in self.c.execute('SELECT * FROM funcionario'):
            print(row)

    def consulta_tabela_funcionarioid(self, nome):
        return self.c.execute('SELECT id_funcionario FROM funcionario WHERE nome =?', (nome,)).fetchone()
        #for row in self.c.execute('SELECT id_funcionario FROM funcionario WHERE nome =?', (nome,)):
         #   print(row)

    def consulta_tabela_veiculo(self):
        return self.c.execute('SELECT * FROM veiculo')
        #for row in self.c.execute('SELECT * FROM veiculo'):
         #   print(row)

    def consulta_tabela_veiculo_placa(self):
        return self.c.execute('SELECT placa FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_entrada(self):
        return self.c.execute('SELECT dia_hora_entrada FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_tipo(self):
        return self.c.execute('SELECT tipo FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_pago(self):
        return self.c.execute('SELECT pago FROM veiculo WHERE pago = 0')

    def consulta_baixa_veiculopago(self):
        return self.c.execute('SELECT pago FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculoplaca(self):
        return self.c.execute('SELECT placa FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculoentrada(self):
        return self.c.execute('SELECT dia_hora_entrada FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculotipo(self):
        return self.c.execute('SELECT tipo FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculonome(self):
        for i in self.c.execute('SELECT nome FROM funcionario INNER JOIN veiculo on veiculo.fk_id_funcionario_caixa = funcionario.id_funcionario WHERE pago > 0 '):
            print(i)
        return self.c.execute('SELECT nome FROM funcionario INNER JOIN veiculo on veiculo.fk_id_funcionario_caixa = funcionario.id_funcionario WHERE pago > 0')

    def consulta_placa(self, placa):
        return self.c.execute("SELECT dia_hora_entrada FROM veiculo WHERE placa=(?) AND pago = 0", (placa,)).fetchone()

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

    def apagar(self):
        self.c.execute("DELETE FROM veiculo WHERE pago=0")
        self.c.commit()
