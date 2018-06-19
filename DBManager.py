from sqlite3 import *
from datetime import *


class DBManager(object):

    def __init__(self):

        self.__path = 'c:\sqlite\estacionamento_bd'
        self.__conn = connect(self.__path + '\estacionamento.db')
        self.__c = self.__conn
        # Criando Tabela de funcionarios
        self.__c.execute('''CREATE TABLE IF NOT EXISTS funcionario
                                    (
                                        id_funcionario INTEGER PRIMARY KEY,
                                        nome TEXT NOT NULL,
                                        turno TEXT NOT NULL,
                                        senha TEXT NOT NULL,
                                        cpf INT NOT NULL        
                                    )''')

        self.__c.commit()

        # Criando tabela de Veiculos
        self.__c.execute('''CREATE TABLE IF NOT EXISTS veiculo
                                            (   
                                                id_veiculo INTEGER PRIMARY KEY,
                                                tipo TEXT NOT NULL,
                                                placa TEXT NOT NULL,
                                                dia_hora_entrada TEXT NOT NULL,
                                                fk_id_funcionario_caixa,
                                                pago INT,
                                                FOREIGN KEY(fk_id_funcionario_caixa) REFERENCES funcionario(id_funcionario)
                                            )''')

        self.__c.commit()

    def close(self):
        self.__conn.close()

    def popular_tabela(self, nome, turno, senha, cpf):
        self.__c.execute("INSERT INTO funcionario (nome, turno, senha, cpf) VALUES (?,?,?,?)", (nome, turno, senha, cpf))
        self.__c.commit()

    def inserir_veiculo(self, placa, entrada, tipo):
        pago = 0
        self.__c.execute("INSERT INTO veiculo (placa, dia_hora_entrada, pago, tipo) VALUES (?,?,?,?)", (placa, entrada, pago, tipo))
        self.__c.commit()

    def pagar(self, placa, tarifa, id_funcionario):
        self.__c.execute("UPDATE veiculo SET pago=?, fk_id_funcionario_caixa =?  WHERE placa=?", (tarifa, id_funcionario, placa))
        self.__c.commit()

    def consulta_tabela(self):
        for row in self.__c.execute('SELECT * FROM funcionario'):
            print(row)

    def consulta_tabela_funcionarioid(self, nome):
        return self.__c.execute('SELECT id_funcionario FROM funcionario WHERE nome =?', (nome,)).fetchone()
        #for row in self.c.execute('SELECT id_funcionario FROM funcionario WHERE nome =?', (nome,)):
         #   print(row)

    def consulta_tabela_veiculo(self):
        return self.__c.execute('SELECT * FROM veiculo')
        #for row in self.c.execute('SELECT * FROM veiculo'):
         #   print(row)

    def consulta_tabela_veiculo_placa(self):
        return self.__c.execute('SELECT placa FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_entrada(self):
        return self.__c.execute('SELECT dia_hora_entrada FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_tipo(self):
        return self.__c.execute('SELECT tipo FROM veiculo WHERE pago = 0')

    def consulta_tabela_veiculo_pago(self):
        return self.__c.execute('SELECT pago FROM veiculo WHERE pago = 0')

    def consulta_baixa_veiculopago(self):
        return self.__c.execute('SELECT pago FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculoplaca(self):
        return self.__c.execute('SELECT placa FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculoentrada(self):
        return self.__c.execute('SELECT dia_hora_entrada FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculotipo(self):
        return self.__c.execute('SELECT tipo FROM veiculo WHERE pago > 0')

    def consulta_baixa_veiculonome(self):
        for i in self.__c.execute('SELECT nome FROM funcionario INNER JOIN veiculo on veiculo.fk_id_funcionario_caixa = funcionario.id_funcionario WHERE pago > 0 '):
            print(i)
        return self.__c.execute('SELECT nome FROM funcionario INNER JOIN veiculo on veiculo.fk_id_funcionario_caixa = funcionario.id_funcionario WHERE pago > 0')

    def consulta_placa(self, placa):
        return self.__c.execute("SELECT dia_hora_entrada FROM veiculo WHERE placa=(?) AND pago = 0", (placa,)).fetchone()

    def valida_login(self, usuario, senha):
        for row in self.__c.execute('SELECT nome, senha FROM funcionario WHERE nome=(?) AND senha=(?)', (usuario, senha)):
            return True
        return False

    def apagar(self):
        self.__c.execute("DELETE FROM veiculo WHERE pago=0")
        self.__c.commit()
