from GUI_MenuPrincipal import *
from tkinter import *
from Veiculo import *
from datetime import *



class Entrada_Veiculo(object):

    def __init__(self):

        self.janela = Tk()
        self.janela.title("Entrada Veiculo")
        self.janela["bg"] = "grey"
        self.janela.geometry("200x200+100+100")

        #Definindo Labels

        self.lbHora = Label(self.janela, text=datetime.today())
        self.lbHora.grid(row=0, column=1, columnspan=2)

        self.lbPlaca = Label(self.janela, text="Placa:")
        self.lbPlaca.grid(row=1, column=1)

        #Definindo Entries

        self.edPlaca = Entry(self.janela)
        self.edPlaca.grid(row=1, column=2)
        self.edPlaca.focus_force()

        #Definindo botao

        self.btok = Button(self.janela, text="Ok", command=self.set_veiculo)
        self.btok.grid(row=2, column=1)

        self.btvoltar = Button(self.janela, text="Voltar", command=self.voltar)
        self.btvoltar.grid(row=2, column=2)

        self.janela.mainloop()

    def set_veiculo(self):
        self.data = str(datetime.today())
        v = Veiculo()
        v.set_placa(self.edPlaca.get(), self.data)

    def voltar(self):
        GUI_MenuPrincipal()
        self.janela.destroy()

