from tkinter import *
from DBManager import *


class Patio(object):
    def __init__(self):
        self.janela = Tk()



        self.btvoltar = Button(self.janela, text="Voltar", command=self.voltar)
        self.btvoltar.grid(row=0, column=2)

        self.banco = DBManager()
        self.alterar()
        self.listaVeiculo()
        self.listaEntrada()
        self.listaPago()
        self.listaTipo()
        self.listaNome()




        # print tabela veiculos para comparação
        #for b in self.banco.consulta_tabela_veiculo():
         #   print(b)


        self.janela.mainloop()

    def voltar(self):
        self.janela.destroy()

    def listaNome(self):
        pass

    def alterar(self):
        self.janela.title("Listagem de Veiculos no patio")
        self.janela.geometry("570x200+450+200")
        self.janela["bg"] = "grey"
        self.lb = Label(self.janela, text="Veiculos com pagamento em aberto")
        self.lb.grid(row=0, column=0, columnspan=2)

    def listaEntrada(self):
        self.lbentrada = Label(self.janela, text="Entrada")
        self.lbentrada.grid(row=2, column=1)

        self.listaentrada = Listbox(self.janela, width=30)
        self.listaentrada.grid(row=3, column=1)
        self.entrada = self.banco.consulta_tabela_veiculo_entrada()
        for e in self.entrada:
            self.listaentrada.insert(END, e)

    def listaTipo(self):
        self.lbtipo = Label(self.janela, text="Tipo")
        self.lbtipo.grid(row=2, column=3)

        self.listatipo = Listbox(self.janela, width=30)
        self.listatipo.grid(row=3, column=3)
        self.tipo = self.banco.consulta_tabela_veiculo_tipo()
        for e in self.tipo:
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

        self.veiculos = self.banco.consulta_tabela_veiculo_placa()
        for i in self.veiculos:
            self.listaplaca.insert(END, i)
