class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente

head = Nodo( 30 )

print( head.data )

head2 = Nodo( 20 )
head2.next = Nodo( 15 )

print(head2.data)

head2 = Nodo( 20, Nodo( 15 ) ) 
