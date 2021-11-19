class NodoDoble:
    def __init__(self, value, anterior=None, siguiente=None):
        self.data = value
        self.pre = anterior
        self.next =siguiente

class DoubleLinkedList():
    def __init__( self):
        self.__head = None
        self.__tail = None
        self.__size = 0 
        self.__head.next = self.__tail
        self.__tail.pre = self.__head
        print( f' head : { self.__head.data }') 
        print( f' head : { self.__tail.data }') 

    def is_empty( self ):
        return self.__size == 0

    def append( self, dato ):
        if self.is_empty():
            self.__head = NodoDoble( dato, None, None )
            self.__tail = self.__head
        else:
            self.tail.next = NodoDoble( dato, None, self.__tail)
        self.__size += 1
         
    def transversal( self ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.next == None:
                print( curr_node.data)
            else: 
                print( curr_node.data , end=" --> ")
            curr_node = curr_node.next
    
    def find