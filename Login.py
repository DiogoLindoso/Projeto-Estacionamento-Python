from MenuPrincipal import *
from tkinter import messagebox
from tkinter import *


class Login(object):
    def __init__(self):
        self.__janela = Tk()
        self.__janela.title("Login")
        self.__janela.geometry("252x80+450+200")

        lbusuario = Label(self.__janela, text="Usuário:", width=10, font="Courier 10")
        lbusuario.grid(row=2, column=1)
        lbsenha = Label(self.__janela, text="Senha:", width=10, font="Courier 10")
        lbsenha.grid(row=3, column=1)

        self.__edusuario = Entry(self.__janela, font="Courier 10")
        self.__edusuario.grid(row=2, column=2)
        self.__edusuario.focus()
        self.__edusuario.bind("<Return>", self.altera_foco)

        self.__edsenha = Entry(self.__janela, show="*", font="Courier 10")
        self.__edsenha.grid(row=3, column=2)
        self.__edsenha.bind("<Return>", self.verificar)

        bt = Button(self.__janela, text="Confirmar", command=self.verificar, font="Courier 10")
        bt.grid(row=4, column=2)

        self.__janela.mainloop()

    def altera_foco(self, a):
        self.__edsenha.focus()

    def verificar(self, a):
        banco = DBManager()
        liberado = banco.valida_login(self.__edusuario.get(), self.__edsenha.get())

        if liberado:
            __usuario = self.__edusuario.get()
            self.__janela.destroy()
            GUIMenuPrincipal(__usuario)
            return True
        else:
            messagebox.showinfo("Aviso", "Usuário ou senha incorreto")
            return False

