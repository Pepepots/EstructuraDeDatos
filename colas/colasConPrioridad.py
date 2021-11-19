from ADTList import LinkedListADT

# Se creo una ADT de lista ligada personalizado para este programa 
class PriorityQueue:
    def __init__(self):
        self.__data = LinkedListADT()

    def isEmpty(self):
        return self.__data.is_empty()
    
    def length(self):
        return self.__data.getTamano()
    
    def enqueue(self, prioridad, dato):
        par = [ prioridad, dato ]

        if self.isEmpty():
            self.__data.append(par)
        else:
            self.__data.agregarSegunPrioridad( prioridad, par)

    def dequeue(self):
        if not self.isEmpty():
            return self.__data.prePop()

    def toString(self):
        self.__data.transversal()


prueba1 = PriorityQueue()
# print(prueba1.isEmpty())
# print(prueba1.length())
prueba1.enqueue(4,'Maestre')
prueba1.enqueue(2,'Niños')
prueba1.enqueue(4,'Mecanico')
prueba1.enqueue(3,'Hombres')
prueba1.enqueue(4,'Vigia')
prueba1.enqueue(5,'Capitan')
prueba1.enqueue(4,'Timonel')
prueba1.enqueue(3,'Mujeres')
prueba1.enqueue(2,'3ra Edad')
prueba1.enqueue(1,'Niñas')
prueba1.toString()

# print('----------------')
# while prueba1.length() != 0:
#     prueba1.dequeue()
#     prueba1.toString()
#     print('----------------')