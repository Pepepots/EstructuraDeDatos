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
                elif row[i] == 'E':
                    str = str + chalk.green( row[i] ) + ' '
                elif row[i] == 'S':
                    str = str + chalk.red( row[i] ) + ' '
                elif row[i] == 'C':
                    str = str + row[i] + ' '
            print(str)
        print('')
        
    def encontrarCamino(self):
        cor = self.respuesta.peek()
        estado = self.tablero.get_item( cor[0], cor[1])
        print(cor)
        print(estado)
        print(self.tablero.get_item( cor[0]-1, cor[1]))
        # while estado != 'S':
        # if self.tablero.get_item( cor[0]-1, cor[1] ) != 'P' and self.tablero.get_item( cor[0]-1, cor[1] ) != 'S':
        #     self.tablero.set_item( cor[0]-1, cor[1], 'V' )
        #     self.respuesta.push([ cor[0]-1, cor[1]])
    
    # def getRespuesta( self ):
        # return( self.respuesta )
    

# entrada = [ 9, 1 ]
# salida = [1,9]
# camino = [(8,1),(8,2),(8,3),(7,3),(6,3),(5,3),(5,2),(4,2),(3,2),(3,1),(3,2),(3,1),(3,1),(3,0),(3,3),(3,4),(3,5),(3,6),(2,5),(1,5),(1,6),(1,7),(8,4),(1,8)]

# prueba1 = Laberinto('entrada.txt')
# prueba1.formato()
# prueba1.encontrarCamino()
# prueba1.formato()
# print( prueba1.getRespuesta().peek() )

txt = open('entrada.txt','rt')
row = int(txt.readline())
col = int(txt.readline())
info = txt.readlines()

for index in range( len(info) ):
    info[index] = info[index].rstrip('\n').split(',')

tablero = ADTArray2D( row, col )
for r in range(row):
    for c in range(col):
            tablero.set_item( r, c, info[r][c] )
        # print( f'({r},{c})')
        
# tablero.to_string()
 
# print(row)
# print(col)
# print(info)