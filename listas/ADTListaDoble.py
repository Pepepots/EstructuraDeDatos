from Nodos import NodoDoble

class DoubleLinkedList():
    def __init__( self):
        self.__head = None
        self.__tail = None
        self.__head.next = self.__tail
        self.__tail.pre = self.__head
        self.__size = 0 
        print( f' head : { self.__head.data }') 
        print( f' head : { self.__tail.data }') 

    def is_empty( self ):
        return self.__size == 0

    def append( self, dato ):
        if self.is_empty():
            self.__head = NodoDoble( dato, None, self.__tail )
         