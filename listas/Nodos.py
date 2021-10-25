class NodoSimple:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente

class NodoDoble:
    def __init__(self, value, anterior=None, siguiente=None):
        self.data = value
        self.pre = anterior
        self.next =siguiente

# head = Nodo( 30 )
# print( head.data )

# head2 = Nodo( 20 )
# head2.next = Nodo( 15 )

# print(head2.data)
# head2 = Nodo( 20, Nodo( 15 ) ) 

# print( head3.next.next.data )

# head4 = Nodo( 5, Nodo(6, Nodo(7,Nodo(8,Nodo(9)))))
# # print( head4.next.next.data )
# curr_node = head4

# # Recorrer
# while curr_node != None :
#     print(curr_node.data)
#     curr_node = curr_node.next    
# # print(curr_node.data)

# Agregar
# curr_node = head4
# while curr_node.next != None :
    # curr_node = curr_node.next    
# curr_node.next = Nodo(10)

# # Eliminar
# curr_node = head4

# while curr_node.next.next != None :
#     curr_node = curr_node.next 
# curr_node.next = None


# print('----------')
# curr_node = head4

# while curr_node != None :
#     print(curr_node.data)
#     curr_node = curr_node.next  


Nodo1 = NodoDoble( 1, None )
Nodo2 = NodoDoble( 2, Nodo1 )
Nodo3 = NodoDoble( 3, Nodo2 )
Nodo4 = NodoDoble( 4, Nodo3 )
Nodo5 = NodoDoble( 5, Nodo4, None )

Nodo1.next = Nodo2
Nodo2.next = Nodo3
Nodo3.next = Nodo4
Nodo4.next = Nodo5

# print( Nodo1.next.data )
# print( Nodo2.pre.data )

head = Nodo1
tail = Nodo5

# Recorrer Ida
curr_node = head

while curr_node != None:
    print( curr_node.data )
    curr_node = curr_node.next 


print('----------')

# Recorrer Final 
curr_node = tail

while curr_node != None:
    print( curr_node.data )
    curr_node = curr_node.pre 