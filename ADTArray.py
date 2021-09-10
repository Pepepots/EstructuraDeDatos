class Array():
    def __init__( self, tamano ):
        self.__tamano = tamano
        self.__data = [0 for x in range(self.__tamano)]

    def get_item( self, index ):
        return self.__data[ index ]

    def to_string( self ):
        print( self.__data )

    def clear ( self, dato ):
        self.__data = [dato for x in range(self.__tamano)]

    def getLenght( self ):
        contador = 0
        for i in self.__data:
            contador = contador + 1
        return contador
    
    

ejemplo = Array(5)

ejemplo.to_string()
ejemplo.get_item(3)
ejemplo.clear(1)
ejemplo.to_string()
print(ejemplo.getLenght())