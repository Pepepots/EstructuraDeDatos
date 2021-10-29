class StackADT:
    def __init__(self):
        self.data = list()
        self.tope = 0

    def isEmpty(self):
        return self.tope == 0

    def length(self):
        return self.tope

    def pop(self):
        if not self.isEmpty():
            self.tope -= 1
            return self.data.pop()

    def peek(self):
        return self.data[ self.tope -1 ]

    def push(self,value):
        self.data.append(value)
        self.tope += 1

    def toString(self):
        for i in self.data:
            print(f'|{ i }|')
        # print('')


# pila = StackADT()
# pila.push(10)
# pila.push(20)
# pila.push(30)
# pila.push(40)
# pila.toString()
# print(f'La pila tiene {pila.length()} elementos')
# pila.pop()
# pila.toString()