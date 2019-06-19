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
   
    def nextFrame(self):
     self.x=[]
     self.y=[]
     self.x.append(0)
     self.y.append(0)
     self.x.append(gridX)
     self.y.append(gridX)
     newcells = []
     for i in range(gridX):
      row = []
      for j in range(gridX):
       row.append(Cell(i,j))
      newcells.append(row)

    def willLive (self,i,j):
      global neighbours
      neighbours = 0;
      for x in [i-1,i,i+1]:
       for y in [j-1,j,j+1]:
        if ( x == i and y == j):
         continue
        if (x != i and y !=j):
         neighbours += self.cells[x][y]
        elif (x == self.x and y != self.y):
         neighbours += self.cells[0][y]
        elif (x != self.x and y == self.y):
         neighbours += self.cells[x][0]
        else:
         neighbours += self.cells[0][0]
      return neighbours
    
    def start(self):
     for i in range (gridX):
      for j in range (gridX):
         live = LiveGame()
         live.willLive(i,j)
         if (self.cells[i][j] == True and live<2):
          self.newcells[i][j] = False
         elif (self.cells[i][j] == True and live == 2):
          self.newcells[i][j] == True
         elif (self.cells[i][j] == True and live > 3):
          self.newcells[i][j] == False
         elif(self.cells[i][j] == False and live == 3):
          self.newcells[i][j] == True

     while True:
      self.nextFrame()
      plt.clf()
      plt.hexbin(self.x, self.y, gridsize=(gridX, gridY), cmap=plt.cm.Purples_r)
      plt.axis('off')
      plt.draw()
      plt.pause(z) #pausa entre cuadricula y cuadricula para mostrar

game = LiveGame()
numero = float(input('Cantidad de celulas vivas:(1-10) '))
n = (numero*0.1)
alive = int(n*gridX*gridX)

x = int(input('Semilla del Aleatorio: '))
random.seed(x)    
for i in range(int(alive)):
   game.cells[random.randint(0,(gridX-1))][random.randint(0,(gridX-1))].viva = True
#genera las condiciones iniciales para la generacion 0
    
game.start()


