class Nodo:
    def __init__(self, value, siguiente=None):
        self.data = value
        self.next = siguiente

    

# head = Nodo( 30 )
# print( head.data )

# head2 = Nodo( 20 )
# head2.next = Nodo( 15 )

# print(head2.data)
# head2 = Nodo( 20, Nodo( 15 ) ) 

# head3 = Nodo( 10, Nodo(20, Nodo(30)))

# print( head3.next.next.data )

# head4 = Nodo( 5, Nodo(6, Nodo(7,Nodo(8,Nodo(9)))))
# # print( head4.next.next.data )
# curr_node = head4

# # Recorrer
# while curr_node != None :
#     print(curr_node.data)
#     curr_node = curr_node.next    
# # print(curr_node.data)

# # Agregar
# # curr_node = head4
# # while curr_node.next != None :
#     # curr_node = curr_node.next    
# # curr_node.next = Nodo(10)

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
