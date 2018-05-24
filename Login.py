import tkinter
from tkinter import *
from DBManager import *
from EntradaVeiculo import *
from GUI_MenuPrincipal import *


class Login(object):
    def __init__(self):

        self.janela = tkinter.Tk()
        self.janela.title("Login")
        self.janela["bg"] = "grey"
        self.janela.geometry("200x80+100+100")

        self.lbusuario = Label(self.janela, text="Usuário:", width=10)
        self.lbusuario.grid(row=2, column=1)
        self.lbsenha = Label(self.janela, text="Senha:", width=10)
        self.lbsenha.grid(row=3, column=1)

        self.edusuario = Entry(self.janela)
        self.edusuario.grid(row=2, column=2)
        self.edusuario.focus_force()
        self.edsenha = Entry(self.janela, show="*")
        self.edsenha.grid(row=3, column=2)

        self.bt = Button(self.janela, text="Confirmar", command=self.verificar)
        self.bt.grid(row=4, column=2)

        self.janela.mainloop()

    def verificar(self):
        banco = DBManager()
        liberado = banco.valida_login(self.edusuario.get(), self.edsenha.get())

        if liberado:
            self.janela.destroy()
            GUI_MenuPrincipal()
            #self.e = Entrada_Veiculo()
