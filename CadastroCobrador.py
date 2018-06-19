from tkinter import *
from tkinter import messagebox
from DBManager import *


class CadastroCobrador(object):
    def __init__(self):
        self.__janela = Tk()
        self.__janela.title("Cadastro Cobrador")
        self.__janela["bg"] = "grey"
        self.__janela.geometry("300x200+450+200")

        self.__lbnome = Label(self.__janela, text="Nome:", width=10, font="Courier 10")
        self.__lbnome.grid(row=0, column=0)

        self.__ednome = Entry(self.__janela, font="Courier 10")
        self.__ednome.grid(row=0, column=1)

        self.__lbturno = Label(self.__janela, text="Turno:", width=10, font="Courier 10")
        self.__lbturno.grid(row=1, column=0)

        self.__edturno = Entry(self.__janela, font="Courier 10")
        self.__edturno.grid(row=1, column=1)

        self.__lbcpf = Label(self.__janela, text="CPF:", width=10, font="Courier 10")
        self.__lbcpf.grid(row=2, column=0)

        self.__edcpf = Entry(self.__janela, font="Courier 10")
        self.__edcpf.grid(row=2, column=1)

        self.__lbsenha = Label(self.__janela, text="Senha:", width=10, font="Courier 10")
        self.__lbsenha.grid(row=3, column=0)

        self.__edsenha = Entry(self.__janela, show="*", font="Courier 10")
        self.__edsenha.grid(row=3, column=1)

        self.__bt = Button(self.__janela, text="Cadastrar", width=10, command=self.cadastrar, font="Courier 10")
        self.__bt.grid(row=4, column=0)

        self.__btvoltar = Button(self.__janela, text="Voltar", width=10, command=self.voltar, font="Courier 10")
        self.__btvoltar.grid(row=4, column=1)

        self.__janela.mainloop()

    def cadastrar(self):

        banco = DBManager()
        banco.popular_tabela(self.__ednome.get(), self.__edturno.get(), self.__edsenha.get(), self.__edcpf.get())
        banco.consulta_tabela()
        self.__ednome.delete(0, END)
        self.__edturno.delete(0, END)
        self.__edcpf.delete(0, END)
        self.__edsenha.delete(0, END)
        messagebox.showinfo("Aviso", "Usuário cadastrado com sucesso")

    def voltar(self):
        self.__janela.destroy()

