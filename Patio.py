from tkinter import *
from DBManager import *


class Patio(object):
    def __init__(self):
        self.janela = Tk()

        self.banco = DBManager()

        self.config()
        self.listaNome()
        self.lista()
        Button(self.janela, text="Voltar", command=self.voltar).grid(row=0, column=2)

        self.janela.mainloop()

    def voltar(self):
        self.janela.destroy()

    def listaNome(self):
        pass

    def config(self):
        self.janela.title("Listagem de Veiculos no patio")
        self.janela.geometry("620x200+450+200")
        lb = Label(self.janela, text="Veiculos com pagamento em aberto")
        lb.grid(row=0, column=0, columnspan=2)

    def lista(self):
        self.listaplaca = Listbox()
        self.listaentrada = Listbox()
        self.listapago = Listbox()
        self.listatipo = Listbox()

        self.listas = [["Placa", self.listaplaca],
                  ["Entrada", self.listaentrada],
                  ["Pago", self.listapago],
                  ["Tipo", self.listatipo]]
        for p, linha in enumerate(self.listas):
            Label(self.janela, text=self.listas[p][0]).grid(row=2, column=p)
            linha[1] = Listbox(self.janela, width=25)
            linha[1].grid(row=3, column=p)
            self.lista_insert(p)

    def lista_insert(self, pos):
        query = [self.banco.consulta_tabela_veiculo_placa(),
                 self.banco.consulta_tabela_veiculo_entrada(),
                 self.banco.consulta_tabela_veiculo_pago(),
                 self.banco.consulta_tabela_veiculo_tipo()]
        for i in query[pos]:
            self.listas[pos][1].insert(END, i)

