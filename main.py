from tkinter import *

from dice import Dice
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application:
    text = "Escolha um dado para sortear"
    bar = FigureCanvasTkAgg

    dice3 = Dice(1, 3)
    dice6 = Dice(1, 6)
    dice12 = Dice(1, 12)
    dice20 = Dice(1, 20)
    dice100 = Dice(1, 100)

    def __init__(self, master=None):
        self.frame = Frame(master)
        self.frame.pack()

        self.titulo = Label(self.frame, text="Randomizador de dados :")
        self.titulo["font"] = self.getFontStyle(size="15", type="bold")
        self.titulo.pack()

        self.resultado = Label(self.frame, text="Resultado")
        self.resultado["font"] = self.getFontStyle(type="italic")
        self.resultado.pack()

        self.msg = Label(self.frame)
        self.msg["text"] = "Escolha um dado para sortear"
        self.msg["font"] = self.getFontStyle(type="italic")
        self.msg.pack()

        self.buttonsDices("Dado 3", self.dice3)
        self.buttonsDices("Dado 6", self.dice6)
        self.buttonsDices("Dado 12", self.dice12)
        self.buttonsDices("Dado 20", self.dice20)
        self.buttonsDices("Dado 100", self.dice100)

        self.buttonShowGraph("Mostrar Valores Dado 3", self.dice3)
        self.buttonShowGraph("Mostrar Valores Dado 6", self.dice6)
        self.buttonShowGraph("Mostrar Valores Dado 12", self.dice12)
        self.buttonShowGraph("Mostrar Valores Dado 20", self.dice20)
        self.buttonShowGraph("Mostrar Valores Dado 100", self.dice100)

        self.buttonExit()

    def buttonsDices(self, text, dice):
        self.random = Button(self.frame, text=text, font=self.getFontStyle(),
                             command=lambda: self.changeText(dice.random()))
        self.random.pack(side=LEFT)

    def buttonShowGraph(self, text, dice):
        self.random = Button(self.frame, text=text, font=self.getFontStyle(),
                             command=lambda: self.showGraph(dice))
        self.random.pack(side=LEFT)
        return

    def showGraph(self, dice):
        if not dice.list_numbers:
            return

        figure = plt.Figure(figsize=(7, 6), dpi=70)

        if type(self.bar) is not type:
            self.bar.get_tk_widget().destroy()

        self.bar = FigureCanvasTkAgg(figure, root)
        self.bar.get_tk_widget().pack(side=RIGHT, fill=BOTH)

        data = {i: dice.list_numbers.count(i) for i in dice.list_numbers}
        df = DataFrame(list(data.items()), columns=['Valores', 'Resultado'])
        df = df[['Valores', 'Resultado']].groupby('Valores').sum()

        ax = figure.add_subplot(111)
        df.plot(kind='bar', legend=True, ax=ax)
        ax.set_title('Dices')

    def changeText(self, number):
        self.msg["text"] = "O número sorteado foi: " + str(number)

    def getFontStyle(self, family="Calibri", size="10", type="normal"):
        return (family, size, type)

    def buttonExit(self):
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

        self.sair = Button(bottomframe)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.frame.quit
        self.sair.pack(side=BOTTOM)


root = Tk()
root.title('Primeiro projeto de Python - Sortear dados')

Application(root)
root.mainloop()
