from tkinter import *
from GUI_Cobrador import *
from EntradaVeiculo import *


class GUI_MenuPrincipal(object):
    def __init__(self):
        self.janelaPrincipal = Tk()
        self.janelaPrincipal.title("Menu Principal")
        self.janelaPrincipal.geometry("500x500+100+100")
        self.janelaPrincipal["bg"] = "grey"

        btcadastro_cobrador = Button(self.janelaPrincipal, text="Cadastro Novo Cobrador", command=self.novo_cobrador)
        btcadastro_cobrador.grid(row=0, column=0)
        btveiculo = Button(self.janelaPrincipal, text="Cadastro Veiculo", command=self.novo_veiculo)
        btveiculo.grid(row=1, column=0)

        self.janelaPrincipal.mainloop()

    def novo_cobrador(self):
        self.janelaPrincipal.destroy()
        GUI_Cobrador()

    def novo_veiculo(self):
        self.janelaPrincipal.destroy()
        Entrada_Veiculo()

