import numpy as np
import matplotlib.pyplot as plt
import random
import time

gridX = int(input("Tamano de X:(multiplo de 6) "))
gridY = int(gridX*0.5)
z = float(input("Tiempo de muestreo:(sg) "))

class Cell:
    def __init__(self, x, y):
        self.viva = False
        self.x = x;
        self.y = y;

class LiveGame:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.cells = []
        for i in range(gridX):
            row = []
            for j in range(gridX):
                row.append(Cell(i,j))
            self.cells.append(row) 
    
    def willLive(self, cell): 
        v =  0;
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
            return True
        else:
            return False

    def nextFrame(self):
        self.x=[]
        self.y=[]
        self.x.append(0)
        self.y.append(0)
        self.x.append(gridX-1)
        self.y.append(gridX)
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
      plt.hexbin(self.x, self.y, gridsize=(gridX,gridY), cmap=plt.cm.binary_r)
      plt.axis("off")
      plt.draw()
      plt.pause(z)

game = LiveGame()
answer1 = input("Quieres elegir la Cantidad de celulas vivas?: ")
if answer1 == "no":
 n1 = random.random()
 n = round(n1,1)
 print ("La proporcion elegida fue: ", n)
elif answer1 == "si":
 n = float(input("Cantidad de celulas vivas:(0-1) "))
else:
 print("Elige si o no")

alive = int(n*gridX*gridX)
print ("alive: ", alive)

answer2 = input("Quieres elegir la Semilla del Aleatorio?: ")
if answer2 == "si":
 x = int(input("Semilla del Aleatorio: "))
 np.random.seed(x)
elif answer2 == "no":
 pass
else:
 print("Elige si o no")
    
for i in range(alive):
   game.cells[np.random.randint(0,(gridX-1))][np.random.randint(0,(gridX-1))].viva = True
    
game.start()


