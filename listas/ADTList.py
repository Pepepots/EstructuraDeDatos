from Nodos import NodoSimple

class LinkedListADT:
    def __init__( self ):
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

    def preAppend( self, dato ):
        tmp = self.head
        self.head = NodoSimple( dato, tmp )

    def transversal( self ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.next == None:
                print( curr_node.data)
            else: 
                print( curr_node.data , end=" --> ")
            curr_node = curr_node.next
    
    def remove( self, dato ):
        curr_node = self.head
        if curr_node != None:
            while curr_node.next != None:
                if curr_node.next.data == dato:
                    # print( curr_node.next.data)
                    if curr_node.next.next != None:
                        # print( curr_node.next.next.data)
                        curr_node.next = curr_node.next.next 
                        # return
                else:
                    curr_node = curr_node.next 
        # return curr_node.data

    def pop( self ):
        curr_node = self.head
        while curr_node.next.next != None :
            curr_node = curr_node.next 
        curr_node.next = None
    
    def prePop( self ):
        self.head = self.head.next

prueba1 = LinkedListADT()
prueba1.append( 0 )
prueba1.append( 1 )
prueba1.append( 2 )
prueba1.append( 3 )
prueba1.preAppend(-1)
prueba1.transversal()
prueba1.pop()
print('------')
prueba1.transversal()
print('------')
prueba1.prePop()
prueba1.transversal()
print('------')
prueba1.remove( 1 )
prueba1.transversal()

