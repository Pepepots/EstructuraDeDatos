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
            str = ' '
            for i in range( len( row )):
                if row[i] == 'P':
                    str = str + chalk.black( row[i] ) + ' '
                elif row[i] == 'E' or row[i] == 'V':
                    str = str + chalk.green( row[i] ) + ' '
                elif row[i] == 'S':
                    str = str + chalk.red( row[i] ) + ' '
                elif row[i] == 'X':
                    str = str + chalk.red( row[i] ) + ' '
                elif row[i] == 'C':
                    str = str + row[i] + ' '
            print(str)
        print('')

    def esLimite(self,cor):
        if cor[ 0 ] >= 0 and cor[ 1 ] >= 0 and cor[ 0 ] < self.tablero.get_row_size() and cor[ 1 ] < self.tablero.get_col_size() :
            return True
        else:
            return False

    def avanzar(self,cor):
        self.tablero.set_item(cor[ 0 ], cor[ 1 ], 'V')
        self.respuesta.push(cor)

    def encontrarCamino(self):
        cor = self.respuesta.peek()
        arriba = [cor[0]-1,cor[1]]
        derecha = [cor[0], cor[1]+1]
        abajo = [cor[0]+1, cor[1]]
        izquierda = [cor[0], cor[1]-1]

        estadoTop = None
        estadoLeft = None
        estadoBot = None
        estadoRigth = None

        # Pregunta si es limite para definir su estado osea si es pared o no 

        if self.esLimite(arriba):
            estadoTop = self.tablero.get_item( arriba[0], arriba[1])
        
        if self.esLimite(derecha):
            estadoLeft = self.tablero.get_item( derecha[0], derecha[1])

        if self.esLimite(abajo):
            estadoBot = self.tablero.get_item( abajo[0], abajo[1])

        if self.esLimite(izquierda):
            estadoRigth = self.tablero.get_item( izquierda[0], izquierda[1])

        # Hacemos la pregunta de donde avanzar si no puede avanzar en ningun lado se regresa una posicion 

        if estadoTop == 'C' or estadoTop == 'S':
            if estadoTop == 'S':
                self.respuesta.push(arriba)
                return
            if estadoTop == 'C':
                self.avanzar(arriba)

        elif estadoLeft == 'C' or estadoLeft == 'S':
            if estadoLeft == 'S':
                self.respuesta.push(derecha)
                return
            if estadoLeft == 'C':
                self.avanzar(derecha)

        elif estadoBot == 'C' or estadoBot == 'S':
            if estadoBot == 'S':
                self.respuesta.push(abajo)
                return
            if estadoBot == 'C':
                self.avanzar(abajo)

        elif estadoRigth == 'C' or estadoRigth == 'S':
            # print(rigth)
            if estadoRigth == 'S':
                self.respuesta.push(izquierda)
                return
            if estadoRigth == 'C':
                # print('si avanzo')
                self.avanzar(izquierda)
        else:
            self.tablero.set_item( cor[ 0 ], cor[ 1 ], 'X')
            self.respuesta.pop()
        
        # self.formato()
        self.encontrarCamino()

    def getRespuesta( self ):
        self.respuesta.toString()
    

prueba1 = Laberinto('entrada.txt')
prueba1.formato()
prueba1.encontrarCamino()
prueba1.formato()
prueba1.getRespuesta()

print('------------------------------------------------------')
prueba2 = Laberinto('entrada2.txt')
prueba2.formato()
prueba2.encontrarCamino()
prueba2.formato()
prueba2.getRespuesta()

print('------------------------------------------------------')
prueba3 = Laberinto('prueba3.txt')
prueba3.formato()
prueba3.encontrarCamino()
prueba3.formato()
prueba3.getRespuesta()

print('------------------------------------------------------')
prueba4 = Laberinto('rebuscado.txt')
prueba4.formato()
prueba4.encontrarCamino()
prueba4.formato()
prueba4.getRespuesta()

