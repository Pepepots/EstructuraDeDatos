class NodoArbolBinario:
    def __init__(self, value, left=None, rigth=None):
        self.data = value
        self.left = left
        self.rigth = rigth

class NodoArbolTernario:
    def __init__(self, value, left=None, center=None, rigth=None):
        self.data = value
        self.left = left
        self.center = center
        self.rigth = rigth