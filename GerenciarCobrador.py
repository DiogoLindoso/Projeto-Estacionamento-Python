from tkinter import *
from DBManager import *
from CadastroCobrador import *


class GerenciarCobrador(object):

    def __init__(self):
        self.__janela = Tk()
        self.__janela.title("Gerenciar Cobradores")
        self.__janela.geometry("450x250+450+200")

        #Rótulos
        __tupla_labels = ("ID", "Nome", "Turno", "CPF")
        for pos, linha in enumerate(__tupla_labels):
            Label(self.__janela, text=__tupla_labels[pos]).grid(row=0, column=pos)

        # Listas
        self.__ltid = Grid
        self.__ltnome = Listbox()
        self.__ltturno = Listbox()
        self.__ltCPF = Listbox()

        self.__lista_listbox = [self.__ltid, self.__ltnome, self.__ltturno, self.__ltCPF]

        for pos, linha in enumerate(self.__lista_listbox):
            self.__lista_listbox[pos] = Listbox(self.__janela, width=15)
            self.__lista_listbox[pos].grid(row=1, column=pos)

        self.lista_insert()

        self.btexcluir = Button()
        self.btatualizar = Button()
        self.btinserir = Button()

        __botoes = [["Excluir", self.excluir, self.btexcluir],
                    ["Atualizar", self.lista_update, self.btatualizar],
                    ["Inserir", self.inserir, self.btinserir]]
        #Botões
        for pos, linha in enumerate(__botoes):
            __botoes[pos][2] = Button(self.__janela, text=__botoes[pos][0], command=__botoes[pos][1])
            __botoes[pos][2].grid(row=2, column=pos)

        self.lista_update()
        self.__janela.mainloop()

    def lista_insert(self):
        banco = DBManager()
        listabanco = banco.consulta_tabela()
        for pos, linha in enumerate(listabanco):
            self.__lista_listbox[0].insert(END, listabanco[pos][0])
            self.__lista_listbox[1].insert(END, listabanco[pos][1])
            self.__lista_listbox[2].insert(END, listabanco[pos][2])
            self.__lista_listbox[3].insert(END, listabanco[pos][4])

    def lista_update(self):

        self.__lista_listbox[0].delete(0, END)
        self.__lista_listbox[1].delete(0, END)
        self.__lista_listbox[2].delete(0, END)
        self.__lista_listbox[3].delete(0, END)
        self.lista_insert()

    def excluir(self):
        selecao = self.__lista_listbox[0].get(ACTIVE)
        banco = DBManager()
        banco.apagar(selecao)
        self.lista_update()

    def inserir(self):
        cobrador = CadastroCobrador()
        cobrador.voltar()
        self.lista_update()
