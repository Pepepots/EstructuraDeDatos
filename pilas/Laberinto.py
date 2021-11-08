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
        # self.tablero.clear( 'P' )
        # self.tablero.set_item( entrada[ 0 ], entrada[ 1 ], 'E' )
        # self.tablero.set_item( salida[ 0 ], salida[ 1 ], 'S' )
        # for par in pasillos:
        #     self.tablero.set_item( par[ 0 ], par[ 1 ], 'C' )
        self.respuesta = StackADT()
        self.buscarEntrada()
        self.respuesta.push(self.entrada)

    def buscarEntrada( self ):
        for r in range(self.row):
            for c in range(self.col):
                tmp = self.tablero.get_item( r, c )
                if tmp == 'E':
                    self.entrada = [ r, c ]


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
        top = [cor[0]-1,cor[1]]
        left = [cor[0], cor[1]+1]
        bot = [cor[0]+1, cor[1]]
        rigth = [cor[0], cor[1]-1]

        estadoTop = None
        estadoLeft = None
        estadoBot = None
        estadoRigth = None

        if self.esLimite(top):
            estadoTop = self.tablero.get_item( top[0], top[1])
        
        if self.esLimite(left):
            estadoLeft = self.tablero.get_item( left[0], left[1])

        if self.esLimite(bot):
            estadoBot = self.tablero.get_item( bot[0], bot[1])

        if self.esLimite(rigth):
            estadoRigth = self.tablero.get_item( rigth[0], rigth[1])

        if estadoTop == 'C' or estadoTop == 'S':
            # print('Si estoy en top')
            if estadoTop == 'S':
                self.respuesta.push(top)
                return
            if estadoTop == 'C':
                self.avanzar(top)

        elif estadoLeft == 'C' or estadoLeft == 'S':
            if estadoLeft == 'S':
                self.respuesta.push(left)
                return
            if estadoLeft == 'C':
                self.avanzar(left)

        elif estadoBot == 'C' or estadoBot == 'S':
            if estadoBot == 'S':
                self.respuesta.push(bot)
                return
            if estadoBot == 'C':
                self.avanzar(bot)

        elif estadoRigth == 'C' or estadoRigth == 'S':
            # print(rigth)
            if estadoRigth == 'S':
                self.respuesta.push(rigth)
                return
            if estadoRigth == 'C':
                # print('si avanzo')
                self.avanzar(rigth)
        else:
            self.tablero.set_item( cor[ 0 ], cor[ 1 ], 'X')
            self.respuesta.pop()

        # print(top)
        # if self.esLimite( top[0], top[1] ):
        #     # print('hoil')
        #     estado = self.tablero.get_item( top[0], top[1] )
        #     if estado == 'S':
        #         self.respuesta.push(top)
        #         return
        #     if estado == 'C':
        #         self.tablero.set_item(top[ 0 ], top[ 1 ], 'V')
        #         self.respuesta.push(top)
        #         # self.encontrarCamino(estado)
        #     elif self.esLimite( left[0], left[1] ) :
        #         estado = self.tablero.get_item( left[0], left[1] )
        #         if estado == 'S':
        #             self.respuesta.push(left)
        #             return
        #         if estado == 'C':
        #             self.tablero.set_item(left[ 0 ], left[ 1 ], 'V')
        #             self.respuesta.push(left)
        #             # self.encontrarCamino(estado)
        #         elif self.esLimite( bot[0], bot[1] ):
        #             estado = self.tablero.get_item( bot[0], bot[1] )
        #             if estado == 'S':
        #                 self.respuesta.push(bot)
        #                 # print('llegue a la solucion')
        #                 return
        #             if estado == 'C':
        #                 self.tablero.set_item(bot[ 0 ], bot[ 1 ], 'V')
        #                 self.respuesta.push(bot)
        #                 # self.encontrarCamino(estado)
        #             elif self.esLimite( rigth[0], rigth[1] ):
        #                 print(rigth)
        #                 estado = self.tablero.get_item( rigth[0], rigth[1] )
        #                 if estado == 'S':
        #                     self.respuesta.push(rigth)
        #                     return
        #                 if estado == 'C':
        #                     self.tablero.set_item(rigth[ 0 ], rigth[ 1 ], 'V')
        #                     self.respuesta.push(rigth)
        #                     # self.encontrarCamino(estado)
        #                 else:
        #                     self.tablero.set_item( cor[ 0 ], cor[ 1 ], 'X')
        #                     self.respuesta.pop()
        # self.formato()
        self.encontrarCamino()
        

        # print(cor)
        # print(estado)
        # print(self.tablero.get_item( cor[0]-1, cor[1]))
        # while estado != 'S':
        # if self.tablero.get_item( cor[0]-1, cor[1] ) != 'P' and self.tablero.get_item( cor[0]-1, cor[1] ) != 'S':
        #     self.tablero.set_item( cor[0]-1, cor[1], 'V' )
        #     self.respuesta.push([ cor[0]-1, cor[1]])
    
    def getRespuesta( self ):
        self.respuesta.toString()
    

# entrada = [ 9, 1 ]
# salida = [1,9]
# camino = [(8,1),(8,2),(8,3),(7,3),(6,3),(5,3),(5,2),(4,2),(3,2),(3,1),(3,2),(3,1),(3,1),(3,0),(3,3),(3,4),(3,5),(3,6),(2,5),(1,5),(1,6),(1,7),(8,4),(1,8)]

prueba1 = Laberinto('entrada.txt')
prueba1.formato()
prueba1.encontrarCamino()
prueba1.getRespuesta()
prueba1.formato()

print('------')
prueba2 = Laberinto('entrada2.txt')
prueba2.formato()
prueba2.encontrarCamino()
prueba2.getRespuesta()
prueba2.formato()

print('------')
prueba3 = Laberinto('prueba3.txt')
prueba3.formato()
prueba3.encontrarCamino()
prueba3.getRespuesta()
prueba3.formato()


# txt = open('entrada.txt','rt')
# row = int(txt.readline())
# col = int(txt.readline())
# info = txt.readlines()

# for index in range( len(info) ):
#     info[index] = info[index].rstrip('\n').split(',')

# tablero = ADTArray2D( row, col )
# for r in range(row):
#     for c in range(col):
#             tablero.set_item( r, c, info[r][c] )
        # print( f'({r},{c})')
        
# tablero.to_string()

# print(row)
# print(col)
# print(info)