import numpy as np
import matplotlib.pyplot as plt
import random


class Cell:
	#Definimos las celdas y sus sistemas de coordenadas
    def __init__(self, x, y):
        self.viva = False
        self.x = x;
        self.y = y;

class LiveGame:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.cells = []
        for i in range(24):#parametro del tamaño de la celda
            row = []
            for j in range(24):
                row.append(Cell(i,j))
            self.cells.append(row) #HAcemos las filas y columnas

    def willLive(self, cell): #definimos una funcion que registra a los vecinos
        vecinos =  0;#usamos un sistema de puntaje que acumula el numero de condiciones punto por punto
        if cell.x+1<24 and self.cells[cell.x+1][cell.y].viva:
            vecinos += 1
        if cell.y+1<24 and self.cells[cell.x][cell.y+1].viva:
            vecinos += 1
        if cell.y-1>=0 and self.cells[cell.x][cell.y-1].viva:
            vecinos += 1
        if cell.y-1<24 and cell.x-1>=0 and self.cells[cell.x-1][cell.y-1].viva:
            vecinos += 1
        if cell.x-1>=0 and self.cells[cell.x-1][cell.y].viva:
            vecinos += 1
        if cell.y+1<24 and cell.x-1>=0 and self.cells[cell.x-1][cell.y+1].viva:
            vecinos += 1
        if vecinos==2 or (cell.viva and vecinos==1):
 #realiza el conteo de los puntos obtenidos, si esta en los limites del conteo la celula esta viva
            return True
        else:
#si el conteo esta fuera de los limites, la celula esta muerta
            return False

    def nextFrame(self):
#realiza la siguiente cuadricula para mostrar las condiciones obtenidas despues de ser aplicada la funcion
        self.x=[]
        self.y=[]
        self.x.append(0)
        self.y.append(0)
        self.x.append(24)
        self.y.append(24)
        newcells = []
        for i in range(24):
            row = []
            for j in range(24):
                row.append(Cell(i,j))
            newcells.append(row)
#acomoda las filas y columnas con las nuevas celulas
        for i in range(24):
            for j in range(24):
                estado = self.willLive(self.cells[i][j])
                newcells[i][j].viva = estado
                if(estado):
                    self.x.append(i)
                    self.y.append(j)
        self.cells = newcells
        self.x = np.array(self.x)
        self.y = np.array(self.y)

    def start(self,gridX = 48,gridY = 24):
        #normaliza la cuadricula
        while True:
                self.nextFrame()
                plt.clf()
                plt.hexbin(self.x, self.y, gridsize=(gridX, gridY), cmap=plt.cm.Blues_r)
                plt.axis('off')
                plt.draw()
#establecimos las caracteristicas fisicas de la cuadricula
                plt.pause(0.1) #pausa entre cuadricula y cuadricula para mostrar
gridX = 48
gridY = 24

game = LiveGame()
numero = float(input('fraccion: '))
#da al usuario para determinar las celulas de la generacion inicial
vivos = int(numero*gridX*gridY)

for i in range(vivos):
   game.cells[random.randint(0,23)][random.randint(0,23)].viva = True
#genera las condiciones iniciales para la generacion 0
game.start()


