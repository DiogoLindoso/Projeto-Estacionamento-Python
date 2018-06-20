from tkinter import *
from tkinter import messagebox
from DBManager import *
from datetime import *


class Calcular(object):
    __placa = ""
    __entrada = ""
    __permanencia = 0

    def __init__(self, usuario):
        self.janela = Tk()
        self.janela.title("Calcular Tarifa")
        self.janela.geometry("400x300+450+200")
        self.usuario = usuario
        lbplaca = Label(self.janela, text="Informe a placa do veiculo:", font="Courier 12")
        lbplaca.grid(row=0, column=0)

        #Caixa de texto
        self.edplaca = Entry(self.janela, width=8, font="Courier 12")
        self.edplaca.grid(row=0, column=1)
        self.edplaca.focus_force()

        #Rótulos
        self.lbentrada = Label(self.janela, text="Tempo de permanência 00:00", width=35, font="Courier 12")
        self.lbentrada.grid(row=2, column=0, columnspan=2)

        self.lbtarifa = Label(self.janela, text="Valor da tarifa = R$ ", width=35, font="Courier 12")
        self.lbtarifa.grid(row=3, column=0, columnspan=2)

        self.lbinfo = Label(self.janela, text="", width=35, font="Courier 12")
        self.lbinfo.grid(row=1, column=0, columnspan=2)

        self.lbnomecobrador = Label(self.janela, text="Cobrador: "+usuario, font="Courier 12", anchor="w")
        self.lbnomecobrador.grid(row=4, column=0)
        #Botões
        btcalc = Button(self.janela, text="Calcular", command=self.setPlaca, font="Courier 12")
        btcalc.grid(row=5, column=0)

        btvoltar = Button(self.janela, text="Voltar", command=self.voltar, font="Courier 12")
        btvoltar.grid(row=5, column=1)

        btpagar = Button(self.janela, text="Pagar", command=self.pagar, font="Courier 12")
        btpagar.grid(row=6, column=1)



        self.janela.mainloop()

    def voltar(self):
        self.janela.destroy()
        
    def setPlaca(self):
        Calcular.__placa = self.edplaca.get().upper()
        if Calcular.__placa != "":

            #Variável __entrada recebe a string com a data e hora de entrada do veiculo
            Calcular.__entrada = self.__get_hora_entrada(Calcular.__placa)

            #Variável __permanencia recebe o tempo total de permanencia em minutos
            Calcular.__permanencia = self.__setPermanencia(Calcular.__entrada)

            # o método privado __calcular_tarifa recebe a permanencia total e retorna o valor da tarifa
            print(Calcular.__placa)
            print(Calcular.__entrada)
            print(f'{Calcular.__permanencia} minutos')
            tarifa = self.__calcular_tarifa(Calcular.__permanencia)
            return tarifa

    def __get_hora_entrada(self, placa):
        try:
            banco = DBManager()
            entrada = banco.consulta_placa(placa)
            Calcular.__entrada = datetime.strptime(entrada[0], '%Y-%m-%d %H:%M:%S.%f')
            return Calcular.__entrada

        except TypeError:
            messagebox.showinfo("Aviso", "Placa não consta no sistema")
            self.edplaca.delete(0, END)
            self.edplaca.focus_force()

    def __setPermanencia(self, datahoraentrada):
        try:
            permanencia = datetime.now()-datahoraentrada
            diaria = False
            if permanencia.days == 0:
                self.tempo = datetime.strptime(str(permanencia), '%H:%M:%S.%f')
            if permanencia.days == 1:
                self.tempo = datetime.strptime(str(permanencia), '%d day, %H:%M:%S.%f')
                diaria = True
            if permanencia.days > 1:
                self.tempo = datetime.strptime(str(permanencia), '%d days, %H:%M:%S.%f')
                diaria = True
            
            self.lbinfo["text"] = "Veiculo placa:" + Calcular.__placa
            perm_text = "Permanência:" + str(permanencia.days) + "D - " + str(self.tempo.hour) + \
                                     "H:" + str(self.tempo.minute) + "M:" + str(self.tempo.second) + "S"
            self.lbentrada["text"] = perm_text

            if diaria:
                totalminutos = ((self.tempo.day * 24) * 60) + (self.tempo.hour * 60) + self.tempo.minute
                return totalminutos
            else:
                totalminutos = (self.tempo.hour * 60) + self.tempo.minute
                return totalminutos

        except TypeError:
            pass
        except AttributeError:
            pass

    def __calcular_tarifa(self, totalminutos):
        # Recebe a permanencia em minutos e retorna o valor da tarifa
        # ate 3 horas = 8 reais para carro ou moto
        # passando de 3 horas 2 reais para cada hora adicional
        try:
            if totalminutos < 30:
                #se o tempo de permanencia for menor q 30 min sera isento
                print("total de minutos"+str(totalminutos))
                self.lbtarifa["text"] = "Valor da tarifa = ISENTO"
                tarifa = int(0)
                return tarifa
            elif totalminutos <= 180:
                # se o tempo de permanencia for ate 3 horas sera taxado em 8 reais
                print("total de minutos" + str(totalminutos))
                self.lbtarifa["text"] = "Valor da tarifa = R$"+str(8.00)
                tarifa = int(8)
                return tarifa
            else:
                # senão o o valor sera de 8 reais + 2 reais por cada hora adicional
                minuto = (totalminutos - 180) % 60
                hora = ((totalminutos - 180) - minuto)/60
                if minuto > 0:
                    #soma 8 + 2 = 10 devido hora com minutos quebrados se  permanencia for de 3 h e 5 min o valor sera de 8 + 2
                    self.lbtarifa["text"] = "Valor da tarifa = R$ "+str(10.00 + (hora * 2))
                    tarifa = int(10 + (hora * 2))
                    return tarifa
                else:

                    print("total de horas passadas"+str(hora+3))
                    self.lbtarifa["text"] = "Valor da tarifa = R$ "+str(8.00+(hora*2))
                    tarifa = int(8+(hora*2))
                    return tarifa
        except TypeError:
            pass

    def pagar(self):
        banco = DBManager()
        # recupera a id do usuário do banco em forma de tupla
        id_usuario = banco.consulta_tabela_funcionarioid(self.usuario)
        #registra no banco os dados do pagamento
        banco.pagar(Calcular.__placa, self.setPlaca(), id_usuario[0])
        #limpa a caixa de texto edplaca
        self.edplaca.delete(0, END)
        #mensagem de aviso para pagamento realizado
        messagebox.showinfo("Aviso", "Pagamento registrado!")


