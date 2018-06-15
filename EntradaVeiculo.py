from tkinter import *
from DBManager import *
from datetime import *
from time import *


class EntradaVeiculo(object):


    def __init__(self, usuario):
        self.janela = Tk()
        self.janela.title("Cadastro Veiculo")
        self.janela.geometry("250x220+450+200")

        #Definindo Labels

        #self.lbHora = Label(self.janela, text="Dia/Hora : "+str(datetime.now()), font="Courier 10")
        self.lbHora = Label(self.janela, text="Dia/Hora : " + strftime('%d/%m/%Y, %H:%M:%S'), font="Courier 10")
        self.lbHora.grid(row=0, column=1, columnspan=2)
        self.relogio()

        #Radio button
        self.tipo = None
        Radiobutton(self.janela, text="Carro", value=1, command=self.set_tipo_carro).grid(row=1, column=1)
        Radiobutton(self.janela, text="Moto", value=2, command=self.set_tipo_moto).grid(row=1, column=2)

        self.lbPlaca = Label(self.janela, text="Placa:", font="Courier 10")
        self.lbPlaca.grid(row=2, column=1)

        #Definindo Entries

        self.edPlaca = Entry(self.janela, font="Courier 10")
        self.edPlaca.grid(row=2, column=2)
        self.edPlaca.focus_force()

        #Definindo botao

        self.btok = Button(self.janela, text="Ok", command=self.set_veiculo, font="Courier 10")
        self.btok.grid(row=3, column=1)

        self.btvoltar = Button(self.janela, text="Voltar", command=self.voltar, font="Courier 10")
        self.btvoltar.grid(row=3, column=2)

        self.janela.mainloop()

    def relogio(self):
        self.lbHora['text'] = "Dia/Hora: " + strftime('%d/%m/%Y, %H:%M:%S')
        self.lbHora.after(1000, self.relogio)  # A cada 1000 milisegundos a funcao relogio sera chamada e a hora sera atualizada !

    def set_tipo_carro(self):
        self.tipo = "carro"

    def set_tipo_moto(self):
        self.tipo = "moto"

    def set_veiculo(self):
        data = datetime.today()
        banco = DBManager()
        print(self.tipo)

        banco.inserir_veiculo(self.edPlaca.get().upper(), data, self.tipo)
        #banco.consulta_tabela_veiculo()

    def voltar(self):
        self.janela.destroy()
