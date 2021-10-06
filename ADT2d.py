class Persona():
    def __init__( self, nom ):
        self.__nom = nom
    
    def get_nombre( self ):
        return self.__nom

class ADTArray2D():
    def __init__( self, row, col ):
        self.__row = row
        self.__col = col
        self.__data = [[] for x in range(self.__row)]
        for i in range( len(self.__data) ):
            self.__data[i] = [1 for x in range(self.__col)]

    def get_info(self):
        return self.__data
    
    def to_string( self ):
        for i in range( len(self.__data) ):
            print( self.__data[i])
    
    def set_item( self, row, col, dato ):
        self.__data[row][col] = dato
    
    def get_item( self, row, col):
        return self.__data[row][col]

    def get_row_size( self ):
        return self.__row

    def get_col_size( self ):
        return self.__col

    def clear( self, dato ):
        for i in range( len(self.__data) ):
            self.__data[i] = [dato for x in range(self.__col)]

    def clearCol( self, col, dato ):
        self.__data[col] = [dato for x in range(self.__col)]



# arr = ADTArray2D( 3, 4 )

# arr.set_item( 0, 0, Persona( 'Pepe' ) )

# # print( arr.get_info() )
# arr.to_string()
# print( arr.get_row_size() )
# print( arr.get_col_size() )
# print( arr.get_item( 2, 2 ) )

# pepe = arr.get_item( 0, 0 )
# print( pepe.get_nombre() )

# arr.clear( 1 )
# arr.to_string()

# # print('Holi')

# # arr.clear( Persona( 'Pepe' ) )
# arr.clearCol( 0, None )
# arr.to_string()