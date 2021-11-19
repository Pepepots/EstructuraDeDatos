class NodoSimple:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente

class LinkedListADT:
    def __init__( self ):
        self.tamano = 0
        self.head = None

    def is_empty( self ):
        return self.head == None

    def get_tail( self ):
        curr_node = self.head
        if curr_node != None:
            while curr_node.next != None:
                curr_node = curr_node.next
        return curr_node

    def append( self , dato ):
        if self.is_empty() :
            self.head = NodoSimple( dato )
        else:
            self.get_tail().next = NodoSimple(dato)
            # tmp = self.get_tail()
            # tmp.next = NodoSimple(dato)
        self.tamano += 1

    def preAppend( self, dato ):
        tmp = self.head
        self.head = NodoSimple( dato, tmp )
        self.tamano += 1
    
    def agregarSegunPrioridad( self, prioridad, dato ):
        curr_node = self.head

        #Este es para que los primeros datos puedan acomodarse de la forma optima
        if curr_node.data[0] > prioridad:
            self.preAppend(dato)
        else:
            #Modificacion del metodo hecho en el examen agregar dato
            while curr_node != None:
                if curr_node.next == None or curr_node.next.data[0] > prioridad:
                    tmp = curr_node.next
                    curr_node.next = NodoSimple(dato,tmp)
                    break
                curr_node = curr_node.next
            self.tamano += 1

    def transversal( self ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.next == None:
                print(f'| {curr_node.data[1]} |')
            else: 
                print(f'| {curr_node.data[1]} | <-- ' , end="")
            curr_node = curr_node.next
    
    def prePop( self ):
        self.head = self.head.next
        self.tamano -= 1

        

    def getTamano( self ):
        return self.tamano

