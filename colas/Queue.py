class Queue:
    def __init__(self):
        self.__data = []

    def isEmpty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.__data.pop(0)
    
    def toString(self):
        for dato in self.__data:
            if dato == self.__data[self.length() - 1]:
                print(f'| {dato} |')
            else:
                print(f'| {dato} | <--', end = '')
            
        print('')


prueba1 = Queue()
prueba1.enqueue(1)
prueba1.enqueue(2)
prueba1.enqueue(3)
prueba1.enqueue(4)
prueba1.toString()
prueba1.dequeue()
prueba1.toString()

print(prueba1.length())