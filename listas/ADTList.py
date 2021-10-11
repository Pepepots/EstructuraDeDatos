from Nodo import Nodo

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
            self.head = Nodo( dato )
        else:
            tmp = self.get_tail()
            tmp.next = Nodo(dato)

    def preAppend( self, dato ):
        tmp = self.head
        self.head = Nodo( dato, tmp )

    def transversal( self ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.next == None:
                print( curr_node.data)
                curr_node = curr_node.next
            else: 
                print( curr_node.data , end=" --> ")
                curr_node = curr_node.next
    
    def remove( self, dato ):
        curr_node = self.head
        if curr_node != None:
            while curr_node.next != None:
                if curr_node.next.data == dato:
                    if curr_node.next.next != None:
                        curr_node.next = curr_node.next.next 
                else:
                    curr_node = curr_node.next 

    def pop( self ):
        curr_node = self.head
        while curr_node.next.next != None :
            curr_node = curr_node.next 
        curr_node.next = None
    
    def prePop( self ):
        self.head = self.head.next



