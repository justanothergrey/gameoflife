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
<<<<<<< HEAD

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
        self.y.append(gridX)
        newcells = []
        for i in range(gridX):
            row = []
            for j in range(gridX):
                row.append(Cell(i,j))
            newcells.append(row)
#acomoda las filas y columnas con las nuevas celulas
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
     
=======
   
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
      for cell.x in [i-1,i,i+1]:
       for cell.y in [j-1,j,j+1]:
        if ( cell.x == i and cell.y == j):
         continue
        if (cell.x != i and cell.y !=j):
         neighbours += oldframe[x][y]
        elif (cell.x == self.x and cell.y != self.y):
         neighbours += oldframe[0][y]
        elif (x != self.x and y == self.y):
         neighbours += oldframe[x][0]
        else:
         neighbours += oldframe[0][0]
      return neighbours
    
>>>>>>> b55427b253356d00733d1bdf7c5fa0f788310813
    def start(self):
     for i in range (gridX):
      for j in range (gridX):
         live = LiveGame()
         live.willLive(i,j)
         if (self.viva[i][j] == True and live<2):
          self.newcells[i][j] = False
         elif (self.viva[i][j] == True and live == 2):
          self.newcells[i][j] == True
         elif (self.viva[i][j] == True and live > 3):
          self.newcells[i][j] == False
         elif(self.viva[i][j] == False and live == 3):
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


