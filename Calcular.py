from tkinter import *
from tkinter import messagebox
from DBManager import *
from datetime import *
from Login import *


class Calcular(object):
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
        btcalc = Button(self.janela, text="Calcular", command=self.guardaPlaca, font="Courier 12")
        btcalc.grid(row=5, column=0)

        btvoltar = Button(self.janela, text="Voltar", command=self.voltar, font="Courier 12")
        btvoltar.grid(row=5, column=1)

        btpagar = Button(self.janela, text="Pagar", command=self.pagar, font="Courier 12")
        btpagar.grid(row=6, column=1)



        self.janela.mainloop()

    def voltar(self):
        self.janela.destroy()
        
    def guardaPlaca(self):
        self.placa = self.edplaca.get().upper()
        if self.placa != "":
            entrada = self.get_hora_entrada(self.placa)
            permanencia_minutos = self.calcular_permanencia(entrada)
            return self.calcular_tarifa(permanencia_minutos)

    def get_hora_entrada(self, placa):
        try:
            banco = DBManager()
            self.entrada = banco.consulta_placa(placa)
            datahoraentrada = datetime.strptime(self.entrada[0], '%Y-%m-%d %H:%M:%S.%f')
            return datahoraentrada

        except (TypeError):
            messagebox.showinfo("Aviso", "Placa não consta no sistema")
            self.edplaca.delete(0, END)

    '''def relogio(self):

        global hora
        global pressionado
        if hora != 0:
            permanencia_minutos = self.calcular_permanencia(hora)
            print(permanencia_minutos)
            tarifa = self.calcular_tarifa(permanencia_minutos)
            print(tarifa)
            t = time
            t.sleep(1)
            self.lbentrada["text"] = "teste"
            self.lbentrada.after(1000, self.relogio())
            print("teste")

        print(pressionado)'''

    def calcular_permanencia(self, datahoraentrada):
        #funcao retorna tempo de permanencia em minutos

        #banco = DBManager()

        #self.entrada = banco.consulta_placa(placa)

        #datahoraentrada = datetime.strptime(self.entrada[0], '%Y-%m-%d %H:%M:%S.%f')
        try:
            permanencia = datetime.now()-datahoraentrada
            #print("dia"+permanencia.day+"hora"+permanencia.hour+"minuto"+permanencia.minute+"segundo"+permanencia.second)
            diaria = False
            if permanencia.days == 0:
                self.tempo = datetime.strptime(str(permanencia), '%H:%M:%S.%f')

            if permanencia.days == 1:
                self.tempo = datetime.strptime(str(permanencia), '%d day, %H:%M:%S.%f')
                diaria = True
            if permanencia.days > 1:
                self.tempo = datetime.strptime(str(permanencia), '%d days, %H:%M:%S.%f')
                diaria = True
            
            self.lbinfo["text"] = "Veiculo placa:" + self.placa
            perm_text = "Permanência:" + str(permanencia.days) + "D - " + str(self.tempo.hour) + \
                                     "H:" + str(self.tempo.minute) + "M:" + str(self.tempo.second) + "S"
            self.lbentrada["text"] = perm_text

            # self.edplaca.delete(0, END)

            if diaria:
                totalminutos = ((self.tempo.day * 24) * 60) + (self.tempo.hour * 60) + self.tempo.minute
                return totalminutos
            else:
                totalminutos = (self.tempo.hour * 60) + self.tempo.minute
                return totalminutos

            #self.lbentrada.after(1000, self.relogio())
        except TypeError:
            pass
        except AttributeError:
            pass


    def calcular_tarifa(self, totalminutos):
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
        id_usuario = banco.consulta_tabela_funcionarioid(self.usuario)
        banco.pagar(self.placa, self.guardaPlaca(), id_usuario[0])


