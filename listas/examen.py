from Nodos import NodoSimple

class listExamen:
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
    
    def transversal( self ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.next == None:
                print( curr_node.data)
            else: 
                print( curr_node.data , end=" --> ")
            curr_node = curr_node.next
    
    def agregarDespuesDelDato( self, prev, dato ):
        curr_node = self.head
        while curr_node != None:
            if curr_node.data == prev:
                tmp = curr_node.next
                curr_node.next = NodoSimple(dato,tmp)
                break
            curr_node = curr_node.next

examen = listExamen()
examen.append(50)
examen.append(55)
examen.append(60)
examen.append(65)
examen.transversal()
examen.agregarDespuesDelDato( 55, 57 )
examen.transversal()
