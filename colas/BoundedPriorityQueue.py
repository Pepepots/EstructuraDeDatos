from Queue import Queue

class BoundedPriorityQueue:
    def __init__(self, niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0
    
    def length(self):
        return self.__size

    # Al ser un array aprobechamos sus prioridades de ordenamiento
    def enqueue(self, prioridad, dato):
        self.__data[prioridad].enqueue(dato)
        self.__size += 1

    # Tenemos que ir recorriendo hasta encontrar uno no vacio para poder sacar de ahi 
    def dequeue(self):
        if not self.isEmpty():
            for nivel in self.__data:
                if not nivel.isEmpty():
                    nivel.dequeue()
                    self.__size -= 1
                    break

    def toString(self):
        for nivel in self.__data:
            # print(nivel)
            nivel.toString()
        print('')
            
prueba1 = BoundedPriorityQueue(7)
# print(prueba1.isEmpty())
# print(prueba1.length())
prueba1.enqueue(4,'Maestre')
prueba1.enqueue(2,'Niños')
prueba1.enqueue(4,'Mecanico')
prueba1.enqueue(3,'Mujeres')
prueba1.enqueue(2,'3ra Edad')
prueba1.enqueue(1,'Niñas')
prueba1.enqueue(3,'Hombres')
prueba1.enqueue(4,'Vigia')
prueba1.enqueue(5,'Capitan')
prueba1.enqueue(4,'Timonel')
prueba1.toString()

# print('----------------')
# while prueba1.length() != 0:
#     prueba1.dequeue()
#     prueba1.toString()
#     print('----------------')