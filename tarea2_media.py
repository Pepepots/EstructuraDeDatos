lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def medio( lista ):
    if len(lista)%2 == 0:
        if len( lista ) == 2:
            lista.pop(1)
            # print( lista )
            return lista
        lista.pop(0)
        lista.pop()
        # print( lista )
        return medio(lista)
    else:
        if len( lista ) == 1:
            return lista
        lista.pop(0)
        lista.pop()
        # print( lista )
        return medio(lista)

print( medio( lista ) )