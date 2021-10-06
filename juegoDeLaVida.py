from yachalk import chalk
from ADT2d import ADTArray2D

class JuegoDeLaVidaADT:
    def __init__( self, rens, cols, list_pob_in, generaciones ):
        self.tablero = ADTArray2D( rens, cols )
        self.generaciones = generaciones
        self.gen = 1
        self.tablero.clear( 'M' )
        self.ren = rens 
        self.col = cols 
        for par in list_pob_in:
            self.tablero.set_item( par[ 0 ], par[ 1 ], 'V' )
        self.corEnTablero()
    
    
    def to_string( self ):
        print( f' --- GENERACION { self.gen } --- ')
        formato = self.tablero.get_info()

        for i in range( len(formato) ):
            row = formato[i]

            str = ''
            for i in range( len( row )):
                if row[i] == '[' or row[i] == ']':
                    str = str + chalk.blue( row[i] )
                elif row[i] == "'" or row[i] == 'M':
                    str = str + chalk.black( row[i] )
                elif row[i] == 'V':
                    str = str + chalk.green( row[i] )
            print(str)

    def get_vecinos(self, r, c):
        vecinos = []
        for ren in range( r-1, r+2, 1 ):
            for col in range( c-1, c+2, 1 ):
                if ren >= 0 and col >= 0 and ren < self.ren and col < self.col :
                    par = [ ren, col ]
                    estePar = [ r, c ]
                    if par != estePar:
                        vecinos.append( [ ren, col ] )
        
        # print(vecinos)
        return vecinos

    def vecinosVivos(self , r, c):
        vecinosVivos = 0
        for par in self.get_vecinos(r, c):
            vecino = self.tablero.get_item( par[0], par[1] )
            if vecino == 'V':
                vecinosVivos += 1
        return vecinosVivos

    def corEnTablero( self ):
        cors = []
        for ren in range( self.ren ):
            for col in range( self.col ):
                cor = [ ren, col ]
                cors.append(cor)
        self.cors = cors 

    def aplicarReglas( self ):
        nuevoEstado = []

        for cor in self.cors:
            vivos = self.vecinosVivos( cor[0], cor[1] )
            estado = self.tablero.get_item( cor[0], cor[1] )
            
            # print(estado)
            # print(vivos)
            if estado == 'V':
                if vivos == 2 or vivos == 3:
                    nuevoEstado.append('V')
                elif vivos == 1 or vivos == 0:
                    nuevoEstado.append('M')
                elif vivos >= 4 :
                    nuevoEstado.append('M')
            elif estado  == 'M':
                if vivos == 3 :
                    nuevoEstado.append('V')
                else:
                    nuevoEstado.append('M')
            # print(nuevoEstado)

        for cor in self.cors:
            self.tablero.set_item( cor[0], cor[1] ,nuevoEstado[0])
            nuevoEstado.pop( 0 )

        self.gen += 1
            # print( self.tablero.get_item( cor[0], cor[1] ) )


# pob_in1 = [(2,2),(3,1),(3,2),(3,3)]

# juego1 = JuegoDeLaVidaADT( 5, 6, pob_in1, 5 )

# for i in range( 5 ):
#     juego1.to_string()
#     juego1.aplicarReglas()

# EXCEL

pob_in2 = [(2,2),(3,1),(3,2),(3,3)]

juego2 = JuegoDeLaVidaADT( 6, 6, pob_in2, 5 )

for i in range( 5 ):
    juego2.to_string()
    juego2.aplicarReglas()


# print('---------')
# print(juego.vecinosVivos( 2, 1 ))
# print('---------')
# print(juego.vecinosVivos( 3, 2 ))
# print('---------')
# print(juego.vecinosVivos( 0, 0 ))
# print('---------')
# print(juego.vecinosVivos( 0, 1 ))
# print('---------')
# print(juego.vecinosVivos( 4, 0 ))

# print(juego.get_vecinos( 4, 0 ))

