from Patio import *


class Baixa(Patio):
    def __init__(self):
        super().__init__()




    def alterar(self):
        self.janela.title("Veículos com baixa")
        self.janela.geometry("750x300+350+200")
        self.lb = Label(self.janela, text="Veiculos com pagamento finalizado")
        self.lb.grid(row=0, column=0, columnspan=2)


    def listaPago(self):

        self.lbpago = Label(self.janela, text="Pago")
        self.lbpago.grid(row=2, column=2)

        self.listapago = Listbox(self.janela)
        self.listapago.grid(row=3, column=2)

        for p in self.banco.consulta_baixa_veiculopago():
            self.listapago.insert(END, p)

    def listaTipo(self):

        self.lbtipo = Label(self.janela, text="Tipo")
        self.lbtipo.grid(row=2, column=3)

        self.listatipo = Listbox(self.janela)
        self.listatipo.grid(row=3, column=3)

        for p in self.banco.consulta_baixa_veiculotipo():
            self.listatipo.insert(END, p)

    def listaVeiculo(self):

        self.lbplaca = Label(self.janela, text="Placa")
        self.lbplaca.grid(row=2, column=0)

        self.listaplaca = Listbox(self.janela)
        self.listaplaca.grid(row=3, column=0)

        for i in self.banco.consulta_baixa_veiculoplaca():
            self.listaplaca.insert(END, i)

    def listaEntrada(self):

        self.lbentrada = Label(self.janela, text="Entrada")
        self.lbentrada.grid(row=2, column=1)

        self.listaentrada = Listbox(self.janela, width=30)
        self.listaentrada.grid(row=3, column=1)

        for e in self.banco.consulta_baixa_veiculoentrada():
            self.listaentrada.insert(END, e)
    def listaNome(self):

        self.lbnome = Label(self.janela, text="Nome caixa")
        self.lbnome.grid(row=2, column=4)

        self.listanome = Listbox(self.janela, width=30)
        self.listanome.grid(row=3, column=4)

        for n in self.banco.consulta_baixa_veiculonome():
            self.listanome.insert(END, n)