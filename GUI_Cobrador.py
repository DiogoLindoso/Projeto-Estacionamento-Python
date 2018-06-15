from tkinter import *
from tkinter import messagebox
from DBManager import *


class GUI_Cobrador(object):
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Cadastro Cobrador")
        self.janela["bg"] = "grey"
        self.janela.geometry("300x200+450+200")

        self.lbnome = Label(self.janela, text="Nome:", width=10, font="Courier 10")
        self.lbnome.grid(row=0, column=0)

        self.ednome = Entry(self.janela, font="Courier 10")
        self.ednome.grid(row=0, column=1)

        self.lbturno = Label(self.janela, text="Turno:", width=10, font="Courier 10")
        self.lbturno.grid(row=1, column=0)

        self.edturno = Entry(self.janela, font="Courier 10")
        self.edturno.grid(row=1, column=1)

        self.lbcpf = Label(self.janela, text="CPF:", width=10, font="Courier 10")
        self.lbcpf.grid(row=2, column=0)

        self.edcpf = Entry(self.janela, font="Courier 10")
        self.edcpf.grid(row=2, column=1)

        self.lbsenha = Label(self.janela, text="Senha:", width=10, font="Courier 10")
        self.lbsenha.grid(row=3, column=0)

        self.edsenha = Entry(self.janela, show="*", font="Courier 10")
        self.edsenha.grid(row=3, column=1)

        self.bt = Button(self.janela, text="Cadastrar", width=10, command=self.cadastrar, font="Courier 10")
        self.bt.grid(row=4, column=0)

        self.btvoltar = Button(self.janela, text="Voltar", width=10, command=self.voltar, font="Courier 10")
        self.btvoltar.grid(row=4, column=1)

        self.janela.mainloop()

    def cadastrar(self):

        banco = DBManager()
        banco.popular_tabela(self.ednome.get(), self.edturno.get(), self.edsenha.get(), self.edcpf.get())
        banco.consulta_tabela()
        self.ednome.delete(0, END)
        self.edturno.delete(0, END)
        self.edcpf.delete(0, END)
        self.edsenha.delete(0, END)
        messagebox.showinfo("Aviso", "Usuário cadastrado com sucesso")

    def voltar(self):
        self.janela.destroy()

