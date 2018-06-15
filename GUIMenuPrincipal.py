from EntradaVeiculo import *
from GUI_Cobrador import *
from Patio import *
from Calcular import *
from tkinter import *
from Baixa import *


class GUIMenuPrincipal(object):
    def __init__(self, usuario):
        self.janela = Tk()
        self.usuario = usuario
        self.janela.title("Menu Principal, Usuário: "+self.usuario)
        self.janela.geometry("500x500+450+200")
        #self.janela["bg"] = "grey"


        btcadastro_cobrador = Button(self.janela, text="Novo Cobrador", command=self.novo_cobrador, width=20, height=3)
        btcadastro_cobrador.grid(row=0, column=0)

        btcadastro_veiculo = Button(self.janela, text="Novo Veiculo", command=self.novo_veiculo, width=20, height=3)
        btcadastro_veiculo.grid(row=1, column=0)

        btpateo = Button(self.janela, text="Patio", command=self.patio, width=20, height=3)
        btpateo.grid(row=2, column=0)

        btcalc = Button(self.janela, text="Calcular", command=self.calc, width=20, height=3)
        btcalc.grid(row=3, column=0)

        btbaixa = Button(self.janela, text="Baixa", command=self.baixa, width=20, height=3)
        btbaixa.grid(row=4, column=0)
        self.janela.mainloop()

    def novo_cobrador(self):
        GUI_Cobrador()

    def novo_veiculo(self):
        EntradaVeiculo(self.usuario)

    def patio(self):
        Patio()

    def calc(self):
        Calcular(self.usuario)
    def baixa(self):
        Baixa()
