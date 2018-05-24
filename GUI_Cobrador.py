from GUI_MenuPrincipal import *
from tkinter import *
from DBManager import *


class GUI_Cobrador(object):
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Cadastro Cobrador")
        self.janela["bg"] = "grey"
        self.janela.geometry("200x200+100+100")

        self.lbnome = Label(self.janela, text="Nome:")
        self.lbnome.grid(row=0, column=0)

        self.ednome = Entry(self.janela)
        self.ednome.grid(row=1, column=0)

        self.lbturno = Label(self.janela, text="Turno:")
        self.lbturno.grid(row=2, column=0)

        self.edturno = Entry(self.janela)
        self.edturno.grid(row=3, column=0)

        self.lbcpf = Label(self.janela, text="CPF:")
        self.lbcpf.grid(row=4, column=0)

        self.edcpf = Entry(self.janela)
        self.edcpf.grid(row=5, column=0)

        self.lbsenha = Label(self.janela, text="Senha:")
        self.lbsenha.grid(row=6, column=0)

        self.edsenha = Entry(self.janela, text="*")
        self.edsenha.grid(row=7, column=0)

        self.bt = Button(self.janela, text="Cadastrar", command=self.cadastrar)
        self.bt.grid(row=8, column=0)

        self.btvoltar = Button(self.janela, text="Voltar", command=self.voltar)
        self.btvoltar.grid(row=8, column=1)
        self.janela.mainloop()

    def cadastrar(self):
        self.banco = DBManager()
        self.banco.popular_tabela(self.ednome.get(), self.edturno.get(), self.edsenha.get(), self.edcpf.get())

    def voltar(self):

        GUI_MenuPrincipal()
        self.janela.destroy()
