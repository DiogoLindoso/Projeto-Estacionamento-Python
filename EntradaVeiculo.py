from tkinter import *
from DBManager import *
from datetime import *
from time import *
from tkinter import messagebox


class EntradaVeiculo(object):

    def __init__(self, usuario):
        self.__janela = Tk()
        self.__janela.title("Cadastro Veiculo")
        self.__janela.geometry("250x220+450+200")

        #Definindo Labels

        #self.lbHora = Label(self.janela, text="Dia/Hora : "+str(datetime.now()), font="Courier 10")
        self.__lbHora = Label(self.__janela, text="Dia/Hora : " + strftime('%d/%m/%Y, %H:%M:%S'), font="Courier 10")
        self.__lbHora.grid(row=0, column=1, columnspan=2)
        self.relogio()

        #Radio button
        self.__tipo = None
        Radiobutton(self.__janela, text="Carro", value=1, command=self.set_tipo_carro).grid(row=1, column=1)
        Radiobutton(self.__janela, text="Moto", value=2, command=self.set_tipo_moto).grid(row=1, column=2)

        self.__lbPlaca = Label(self.__janela, text="Placa:", font="Courier 10")
        self.__lbPlaca.grid(row=2, column=1)

        #Definindo Entries

        self.__edPlaca = Entry(self.__janela, font="Courier 10")
        self.__edPlaca.grid(row=2, column=2)
        self.__edPlaca.focus_force()

        #Definindo botao

        self.__btok = Button(self.__janela, text="Ok", command=self.set_veiculo, font="Courier 10")
        self.__btok.grid(row=3, column=1)

        self.__btvoltar = Button(self.__janela, text="Voltar", command=self.voltar, font="Courier 10")
        self.__btvoltar.grid(row=3, column=2)

        self.__janela.mainloop()

    def relogio(self):
        self.__lbHora['text'] = "Dia/Hora: " + strftime('%d/%m/%Y, %H:%M:%S')
        self.__lbHora.after(1000, self.relogio)  # A cada 1000 milisegundos a funcao relogio sera chamada e a hora sera atualizada !

    def set_tipo_carro(self):
        self.__tipo = "carro"

    def set_tipo_moto(self):
        self.__tipo = "moto"

    def set_veiculo(self):
        data = datetime.today()
        banco = DBManager()

        banco.inserir_veiculo(self.__edPlaca.get().upper(), data, self.__tipo)
        messagebox.showinfo('Aviso', 'Veículo inserido com sucesso!')
        self.__edPlaca.focus_force()
        self.__edPlaca.delete(0, END)
        #banco.consulta_tabela_veiculo()

    def voltar(self):
        self.__janela.destroy()
