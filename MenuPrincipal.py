from EntradaVeiculo import *
from CadastroCobrador import *
from Patio import *
from Calcular import *
from tkinter import *
from Baixa import *


class GUIMenuPrincipal(object):
    def __init__(self, usuario):
        self.__janela = Tk()
        self.__usuario = usuario
        self.__janela.title("Menu Principal, Usuário: " + self.__usuario)
        self.__janela.geometry("500x500+450+100")
        self.__janela.focus_force()
        btcadastro_cobrador = Button(self.__janela, text="Novo Cobrador", command=self.novo_cobrador, width=20, height=3)
        btcadastro_cobrador.grid(row=0, column=0)

        btcadastro_veiculo = Button(self.__janela, text="Novo Veiculo", command=self.novo_veiculo, width=20, height=3)
        btcadastro_veiculo.grid(row=1, column=0)

        btpateo = Button(self.__janela, text="Patio", command=self.patio, width=20, height=3)
        btpateo.grid(row=2, column=0)

        btcalc = Button(self.__janela, text="Calcular", command=self.calc, width=20, height=3)
        btcalc.grid(row=3, column=0)

        btbaixa = Button(self.__janela, text="Baixa", command=self.baixa, width=20, height=3)
        btbaixa.grid(row=4, column=0)
        self.__janela.mainloop()

    def novo_cobrador(self):
        CadastroCobrador()

    def novo_veiculo(self):
        EntradaVeiculo(self.__usuario)

    def patio(self):
        Patio()

    def calc(self):
        Calcular(self.__usuario)

    def baixa(self):
        Baixa()
