lista = [ 1, 2, 3, 4, 5, 6]

def suma( lista ):
    if len(lista) == 0:
        return 0
    # num = lista.pop()
    # print(num)
    # print(lista)
    return lista.pop() + suma(lista)
    
print(suma( lista))