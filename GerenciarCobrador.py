from tkinter import *
from DBManager import *
from CadastroCobrador import *


class GerenciarCobrador(object):
    __b = DBManager()

    def __init__(self):
        __janela = Tk()
        __janela.title("Gerenciar Cobradores")
        __janela.geometry("450x250+450+200")

        #Rótulos
        Label(__janela, text="ID").grid(row=0, column=0)
        Label(__janela, text="Nome").grid(row=0, column=1)
        Label(__janela, text="Turno").grid(row=0, column=2)
        Label(__janela, text="CPF").grid(row=0, column=3)



        #Listas
        self.__ltid = Listbox(__janela, width=8)
        self.__ltid.grid(row=1, column=0)
        self.__ltnome = Listbox(__janela)
        self.__ltnome.grid(row=1, column=1)
        self.__ltturno = Listbox(__janela)
        self.__ltturno.grid(row=1, column=2)
        self.__ltCPF = Listbox(__janela)
        self.__ltCPF.grid(row=1, column=3)

        #Botões
        Button(__janela, text="Excluir", command=self.excluir).grid(row=2, column=0)
        Button(__janela, text="Editar").grid(row=2, column=1)
        Button(__janela, text="Inserir", command=self.inserir).grid(row=2, column=2)

        listabanco = GerenciarCobrador.__b.consulta_tabela()

        print(listabanco)

        for pos, linha in enumerate(listabanco):
            self.__ltid.insert(END, listabanco[pos][0])
            self.__ltnome.insert(END, listabanco[pos][1])
            self.__ltturno.insert(END, listabanco[pos][2])
            self.__ltCPF.insert(END, listabanco[pos][4])

        __janela.mainloop()

    def excluir(self):
        selecao = self.__ltid.get(ACTIVE)
        GerenciarCobrador.__b.apagar(selecao)
        print(selecao)

    def inserir(self):
        inserir = CadastroCobrador()
        inserir.cadastrar()
#GerenciarCobrador()