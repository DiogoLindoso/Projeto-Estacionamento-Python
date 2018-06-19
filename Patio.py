from tkinter import *
from DBManager import *


class Patio(object):
    def __init__(self):
        self.janela = Tk()

        self.banco = DBManager()

        self.alterar()
        self.listaVeiculo()
        self.listaEntrada()
        self.listaPago()
        self.listaTipo()
        self.listaNome()

        self.btvoltar = Button(self.janela, text="Voltar", command=self.voltar)
        self.btvoltar.grid(row=0, column=2)

        self.janela.mainloop()

    def voltar(self):
        self.janela.destroy()

    def listaNome(self):
        pass

    def alterar(self):
        self.janela.title("Listagem de Veiculos no patio")
        self.janela.geometry("620x200+450+200")
        lb = Label(self.janela, text="Veiculos com pagamento em aberto")
        lb.grid(row=0, column=0, columnspan=2)

    def listaEntrada(self):
        self.lbentrada = Label(self.janela, text="Entrada")
        self.lbentrada.grid(row=2, column=1)

        self.listaentrada = Listbox(self.janela, width=30)
        self.listaentrada.grid(row=3, column=1)

        for e in self.banco.consulta_tabela_veiculo_entrada():
            self.listaentrada.insert(END, e)

    def listaTipo(self):
        self.lbtipo = Label(self.janela, text="Tipo")
        self.lbtipo.grid(row=2, column=3)

        self.listatipo = Listbox(self.janela, width=30)
        self.listatipo.grid(row=3, column=3)

        for e in self.banco.consulta_tabela_veiculo_tipo():
            self.listatipo.insert(END, e)

    def listaPago(self):
        self.lbpago = Label(self.janela, text="Pago")
        self.lbpago.grid(row=2, column=2)

        self.listapago = Listbox(self.janela)
        self.listapago.grid(row=3, column=2)

        for p in self.banco.consulta_tabela_veiculo_pago():
            self.listapago.insert(END, p)

    def listaVeiculo(self):
        self.lbplaca = Label(self.janela, text="Placa")
        self.lbplaca.grid(row=2, column=0)

        self.listaplaca = Listbox(self.janela)
        self.listaplaca.grid(row=3, column=0)

        for i in self.banco.consulta_tabela_veiculo_placa():
            self.listaplaca.insert(END, i)
