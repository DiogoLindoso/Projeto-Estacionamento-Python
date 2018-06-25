from Patio import *


class Baixa(Patio):
    def __init__(self):
        super().__init__()

    def config(self):
        self.janela.title("Veículos com baixa")
        self.janela.geometry("750x300+350+200")
        self.lb = Label(self.janela, text="Veiculos com pagamento finalizado")
        self.lb.grid(row=0, column=0, columnspan=2)

    def listaNome(self):

        self.lbnome = Label(self.janela, text="Nome caixa")
        self.lbnome.grid(row=2, column=4)

        self.listanome = Listbox(self.janela, width=30)
        self.listanome.grid(row=3, column=4)

        for n in self.banco.consulta_baixa_veiculonome():
            self.listanome.insert(END, n)

    def lista_insert(self, pos):
        query = [self.banco.consulta_baixa_veiculoplaca(),
                 self.banco.consulta_baixa_veiculoentrada(),
                 self.banco.consulta_baixa_veiculopago(),
                 self.banco.consulta_baixa_veiculotipo()]
        for i in query[pos]:
            print(i)
            self.listas[pos][1].insert(END, i)
