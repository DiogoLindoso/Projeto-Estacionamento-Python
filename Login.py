import tkinter
from tkinter import *
from DBManager import *
from EntradaVeiculo import *
from GUIMenuPrincipal import *


class Login(object):
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Login")
        self.janela["bg"] = "grey"
        self.janela.geometry("252x80+450+200")

        lbusuario = Label(self.janela, text="Usuário:", width=10, font="Courier 10")
        lbusuario.grid(row=2, column=1)
        lbsenha = Label(self.janela, text="Senha:", width=10, font="Courier 10")
        lbsenha.grid(row=3, column=1)

        self.edusuario = Entry(self.janela, font="Courier 10")
        self.edusuario.grid(row=2, column=2)
        self.edusuario.focus_force()
        self.edsenha = Entry(self.janela, show="*", font="Courier 10")
        self.edsenha.grid(row=3, column=2)

        bt = Button(self.janela, text="Confirmar", command=self.verificar, font="Courier 10")
        bt.grid(row=4, column=2)

        self.janela.mainloop()

    def verificar(self):
        banco = DBManager()
        liberado = banco.valida_login(self.edusuario.get(), self.edsenha.get())

        if liberado:
            usuario = self.edusuario.get()
            self.janela.destroy()
            GUIMenuPrincipal(usuario)

            return True
        else:
            print("Erro")
            return False

    def get_usuario(self):
        return str(self.edusuario.get())
