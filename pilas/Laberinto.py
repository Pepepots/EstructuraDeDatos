import os
import time
import platform
from yachalk import chalk
from ADT2d import ADTArray2D
from pilas import StackADT


class Laberinto:
    def __init__( self, ruta ):
        self.read(ruta)
        self.tablero = ADTArray2D( self.row, self.col )
        for r in range(self.row):
            for c in range(self.col):
                self.tablero.set_item( r, c, self.info[r][c] )

        self.respuesta = StackADT()
        self.buscarEntrada()
        self.formato()
        self.limpiar()

    def buscarEntrada( self ):
        for r in range(self.row):
            for c in range(self.col):
                tmp = self.tablero.get_item( r, c )
                if tmp == 'E':
                    self.entrada = [ r, c ]
        self.respuesta.push(self.entrada)

    def read(self,ruta):
        txt = open(ruta,'rt')
        self.row = int(txt.readline())
        self.col = int(txt.readline())
        self.info = txt.readlines()

        for index in range( len(self.info) ):
            self.info[index] = self.info[index].rstrip('\n').split(',')

    def formato( self ):
        formato = self.tablero.get_info()

        for i in range( len(formato) ):
            row = formato[i]
            pared = chalk.black
            entrada = chalk.green_bright
            valido =  chalk.green
            salida = chalk.red_bright
            invalido = chalk.red

            for i in range( len( row )):
                if row[i] == 'P':
                    print(pared(row[i]), end=' ')
                elif row[i] == 'E':
                    print(entrada(row[i]), end=' ')
                    # str = str + chalk.green( row[i] ) + ' '
                elif row[i] == 'V':
                    print(valido(row[i]), end=' ')
                elif row[i] == 'S':
                    print(salida(row[i]), end=' ')
                    # str = str + chalk.red( row[i] ) + ' '
                elif row[i] == 'X':
                    print(invalido(row[i]), end=' ')
                    # str = str + chalk.red( row[i] ) + ' '
                elif row[i] == 'C':
                    print(row[i], end=' ')
                    # str = str + row[i] + ' '
            print('')
        print('')

    def esLimite(self,cor):
        if cor[ 0 ] >= 0 and cor[ 1 ] >= 0 and cor[ 0 ] < self.tablero.get_row_size() and cor[ 1 ] < self.tablero.get_col_size() :
            return True
        else:
            return False

    def avanzar(self,cor):
        self.tablero.set_item(cor[ 0 ], cor[ 1 ], 'V')
        self.respuesta.push(cor)

    def limpiar(self):
        if platform.system() == "Windows":
            self.clear = 'cls' 
        else:
            self.clear = 'clear'

    def encontrarCamino(self):
        os.system(self.clear)
        cor = self.respuesta.peek()
        arriba = [cor[0]-1,cor[1]]
        derecha = [cor[0], cor[1]+1]
        abajo = [cor[0]+1, cor[1]]
        izquierda = [cor[0], cor[1]-1]

        estadoArriba = None
        estadoDerecha = None
        estadoAbajo = None
        estadoIzquierda = None

        # Pregunta si es limite para definir su estado osea si es pared o no 

        if self.esLimite(arriba):
            estadoArriba = self.tablero.get_item( arriba[0], arriba[1])
        
        if self.esLimite(derecha):
            estadoDerecha = self.tablero.get_item( derecha[0], derecha[1])

        if self.esLimite(abajo):
            estadoAbajo = self.tablero.get_item( abajo[0], abajo[1])

        if self.esLimite(izquierda):
            estadoIzquierda = self.tablero.get_item( izquierda[0], izquierda[1])

        # Hacemos la pregunta de donde avanzar si no puede avanzar en ningun lado se regresa una posicion 

        if estadoArriba == 'C' or estadoArriba == 'S':
            if estadoArriba == 'S':
                self.respuesta.push(arriba)
                return
            if estadoArriba == 'C':
                self.avanzar(arriba)

        elif estadoDerecha == 'C' or estadoDerecha == 'S':
            if estadoDerecha == 'S':
                self.respuesta.push(derecha)
                return
            if estadoDerecha == 'C':
                self.avanzar(derecha)

        elif estadoAbajo == 'C' or estadoAbajo == 'S':
            if estadoAbajo == 'S':
                self.respuesta.push(abajo)
                return
            if estadoAbajo == 'C':
                self.avanzar(abajo)

        elif estadoIzquierda == 'C' or estadoIzquierda == 'S':
            # print(rigth)
            if estadoIzquierda == 'S':
                self.respuesta.push(izquierda)
                return
            if estadoIzquierda == 'C':
                # print('si avanzo')
                self.avanzar(izquierda)
        else:
            self.tablero.set_item( cor[ 0 ], cor[ 1 ], 'X')
            self.respuesta.pop()
        
        self.formato()
        time.sleep(.8)

        self.encontrarCamino()

    def getRespuesta( self ):
        self.respuesta.toString()
    

prueba1 = Laberinto('entrada.txt')
# prueba1.formato()
prueba1.encontrarCamino()
# prueba1.formato()
prueba1.getRespuesta()

print('------------------------------------------------------')
prueba2 = Laberinto('entrada2.txt')
# prueba2.formato()
prueba2.encontrarCamino()
# prueba2.formato()
prueba2.getRespuesta()

print('------------------------------------------------------')
prueba3 = Laberinto('prueba3.txt')
# prueba3.formato()
prueba3.encontrarCamino()
# prueba3.formato()
prueba3.getRespuesta()

print('------------------------------------------------------')
prueba4 = Laberinto('rebuscado.txt')
# prueba4.formato()
prueba4.encontrarCamino()
# prueba4.formato()
prueba4.getRespuesta()

