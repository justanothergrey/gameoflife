import numpy as np
import matplotlib.pyplot as plt
import random

gridX = int(input('Tamaño de X:(multiplo de 6) '))
gridY = int(gridX*0.5)
z = float(input('Tiempo de muestreo:(sg) '))

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
        for i in range(gridX):#parametro del tamaño de la celda
            row = []
            for j in range(gridX):
                row.append(Cell(i,j))
            self.cells.append(row) #HAcemos las filas y columnas
    
    def willLive(self, cell): #definimos una funcion que registra a los vecinos
        v =  0;#usamos un sistema de puntaje que acumula el numero de condiciones punto por punto
        if cell.x+1<gridX and self.cells[cell.x+1][cell.y].viva:
            v += 1 #1 
        if cell.y-1 and self.cells[cell.x][cell.y-1].viva:
            v += 1 #2
        if cell.y-1<gridX and cell.x-1>=0 and self.cells[cell.x-1][cell.y-1].viva:
            v += 1 #3
        if cell.x-1 and self.cells[cell.x-1][cell.y].viva:
            v += 1 #4
        if cell.y+1<gridX and cell.x-1>=0 and self.cells[cell.x-1][cell.y+1].viva:
            v += 1 #5
        if cell.y+1<gridX and self.cells[cell.x][cell.y+1]:
            v += 1 #6
        if v==3 or (cell.viva and v==2):
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
        self.x.append(gridX)
        self.y.append(gridY)
        newcells = []
        for i in range(gridX):
            row = []
            for j in range(gridX):
                row.append(Cell(i,j))
            newcells.append(row)
        for i in range(gridX):
            for j in range(gridX):
                estado = self.willLive(self.cells[i][j])
                newcells[i][j].viva = estado
                if(estado):
                    self.x.append(i)
                    self.y.append(j)
        self.cells = newcells
        self.x = np.array(self.x)
        self.y = np.array(self.y)
    
    def start(self):
     while True: 
      self.nextFrame()
      plt.clf()
      plt.hexbin(self.x, self.y, gridsize=(gridX,gridY), cmap=plt.cm.Blues_r)
      plt.axis('off')
      plt.draw()
      plt.pause(z)

game = LiveGame()
answer1 = input('Quieres elegir la Cantidad de celulas vivas?: ')
if answer1 == 'no':
 n = random.random()
elif answer1 == 'si':
 n = float(input('Cantidad de celulas vivas:(0-1) '))
else:
 print('Elige si o no')

alive = int(n*gridX*gridX)

answer2 = input('Quieres elegir la Semilla del Aleatorio?: ')
if answer2 == 'si':
 x = int(input('Semilla del Aleatorio: '))
 np.random.seed(x)
elif answer2 == 'no':
 pass
else:
 print('Elige si o no')
    
for i in range(alive):
   game.cells[np.random.randint(0,(gridX-1))][np.random.randint(0,(gridX-1))].viva = True
    
game.start()


