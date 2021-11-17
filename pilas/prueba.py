class listaLigada:
    
    def __init__(self,n):            
        self.datos=[]
        self.tam=n
        self.vacia=True
        self.llena=False
        self.elementos=0
        self.inicio=0
        for i in range(n):
            self.datos.append([])
            
    def aniadir(self,dato,tipo="final",indice=0):
        if(tipo=="final"):
            if(not self.llena):
                if(self.vacia):
                    self.datos[0]=[dato,-1]
                    self.elementos+=1
                    if(self.elementos==self.tam):
                        self.llena=True
                    self.vacia=False
                else:
                    #Buscar el final de mi lista
                    final=0
                    indice=self.inicio
                    while(not final==-1):
                        if(self.datos[indice][1]==-1):
                            final=-1
                        else:
                            indice=self.datos[indice][1]
                    
                    #Buscar un espacio vacío
                    ubicacionNueva=-1
                    j=0
                    while(ubicacionNueva==-1):
                       if(self.datos[j]==[]):
                           ubicacionNueva=j
                       j+=1
                    
                    #Añadir dato al final de la lista
                    self.datos[indice][1]=ubicacionNueva
                    self.datos[ubicacionNueva]=[dato,-1]
                    self.elementos+=1
                    if(self.elementos==self.tam):
                        self.llena=True
                    self.vacia=False
            else:
                print("La lista está llena")
                
        if(tipo=="inicio"):
            if(not self.llena):
                if(self.vacia):
                    self.datos[0]=[dato,-1]
                    self.elementos+=1
                    if(self.elementos==self.tam):
                        self.llena=True
                    self.vacia=False
                else:
                    #Buscar un espacio vacío
                    ubicacionNueva=-1
                    j=0
                    while(ubicacionNueva==-1):
                       if(self.datos[j]==[]):
                           ubicacionNueva=j
                       j+=1
                    
                    #Añadir dato al inicio de la lista
                    self.datos[ubicacionNueva]=[dato,self.inicio]
                    self.inicio=ubicacionNueva
                    self.elementos+=1
                    if(self.elementos==self.tam):
                        self.llena=True
                    self.vacia=False
            else:
                print("La lista está llena")
        
        if(tipo=="indice"):
            if(not self.llena):
                if(self.vacia):
                    if(indice<self.tam):
                        self.datos[indice]=[dato,-1]
                        self.elementos+=1
                        self.inicio=indice
                        if(self.elementos==self.tam):
                            self.llena=True
                        self.vacia=False
                    else:
                        print("El índice excede el tamaño de la lista")
                else:
                    if(indice<self.tam):
                        #Preguntar si está vacío
                        if(self.datos[indice]==[]):
                            #Buscar el final de mi lista
                            final=0
                            actual=self.inicio
                            while(not final==-1):
                                if(self.datos[actual][1]==-1):
                                    final=-1
                                else:
                                    actual=self.datos[actual][1]
                                    
                            #Añadir dato al final
                            self.datos[actual][1]=indice
                            self.datos[indice]=[dato,-1]
                            self.elementos+=1
                            if(self.elementos==self.tam):
                                self.llena=True
                            self.vacia=False
                        else:
                            #Buscar un espacio vacío
                            ubicacionNueva=-1
                            j=0
                            while(ubicacionNueva==-1):
                               if(self.datos[j]==[]):
                                   ubicacionNueva=j
                               j+=1
                            
                            #Añadir dato frente al elemento que estaba en esa posición
                            self.datos[ubicacionNueva]=[dato,self.datos[indice][1]]
                            self.datos[indice][1]=ubicacionNueva
                            self.elementos+=1
                            if(self.elementos==self.tam):
                                self.llena=True
                            self.vacia=False                   
                    else:
                        print("El índice excede el tamaño de la lista")
            else:
                print("La lista está llena")


    def sacar(self,tipo="final",elem=""):
        if(not(self.vacia)):
            if(tipo=="inicio"):
                dato=self.datos[self.inicio][0]
                nuevoInicio=self.datos[self.inicio][1]
                self.datos[self.inicio]=[]
                self.inicio=nuevoInicio
                self.elementos-=1
                if(self.elementos==0):
                    self.vacia=True
                    self.inicio=0
                self.llena=False
                return dato
            
            if(tipo=="final"):
                #Buscar el penúltimo y el último elemento de mi lista
                if(self.elementos>1):
                    final=0
                    actual=self.inicio
                    while(not final==-1):
                        if(self.datos[self.datos[actual][1]][1]==-1):
                            final=-1
                        else:
                            actual=self.datos[actual][1]
                    final=self.datos[actual][1]
                    
                    #Sacar elemento
                    dato=self.datos[final][0]
                    self.datos[final]=[]
                    self.datos[actual][1]=-1
                    self.elementos-=1
                    if(self.elementos==0):
                        self.vacia=True
                        self.inicio=0
                    self.llena=False
                    return dato
                else:
                    #Buscar único elemento
                    final=0
                    actual=self.inicio
                    while(not final==-1):
                        if(self.datos[actual][1]==-1):
                            final=-1
                        else:
                            actual=self.datos[actual][1]
                    #Sacar elemento
                    dato=self.datos[actual][0]
                    self.datos[actual]=[]
                    self.elementos-=1
                    if(self.elementos==0):
                        self.vacia=True
                        self.inicio=0
                    self.llena=False
                    return dato
            if(tipo=="elemento"):
                if(not(self.vacia)):
                    #Buscar elemento
                    actual=self.inicio
                    final=0
                    encontrado=False
                    while(not(final==-1) and not(encontrado)):
                        if(self.datos[actual][0]==elem):
                            encontrado=True
                        else:
                            actual=self.datos[actual][1]
                            final=actual
                    if(encontrado):
                        if(actual==self.inicio):
                            dato=self.datos[self.inicio][0]
                            nuevoInicio=self.datos[self.inicio][1]
                            self.datos[self.inicio]=[]
                            self.inicio=nuevoInicio
                            self.elementos-=1
                            if(self.elementos==0):
                                self.vacia=True
                                self.inicio=0
                            self.llena=False
                            return dato
                        if(self.datos[actual][1]==-1):
                            #Buscar el penúltimo y el último elemento de mi lista
                            if(self.elementos>1):
                                final=0
                                actual=self.inicio
                                while(not final==-1):
                                    if(self.datos[self.datos[actual][1]][1]==-1):
                                        final=-1
                                    else:
                                        actual=self.datos[actual][1]
                                final=self.datos[actual][1]
                                
                                #Sacar elemento
                                dato=self.datos[final][0]
                                self.datos[final]=[]
                                self.datos[actual][1]=-1
                                self.elementos-=1
                                if(self.elementos==0):
                                    self.vacia=True
                                    self.inicio=0
                                self.llena=False
                                return dato
                            else:
                                #Buscar único elemento
                                final=0
                                actual=self.inicio
                                while(not final==-1):
                                    if(self.datos[actual][1]==-1):
                                        final=-1
                                    else:
                                        actual=self.datos[actual][1]
                                #Sacar elemento
                                dato=self.datos[actual][0]
                                self.datos[actual]=[]
                                self.elementos-=1
                                if(self.elementos==0):
                                    self.vacia=True
                                    self.inicio=0
                                self.llena=False
                                return dato
                        else:
                            #Buscar el elemento anterior al que quiero eliminar
                            final=0
                            previo=self.inicio
                            while(not final==-1):
                                if(self.datos[previo][1]==actual):
                                    final=-1
                                else:
                                    previo=self.datos[previo][1]
                            self.datos[previo][1]=self.datos[actual][1]
                            #Sacar elemento
                            dato=self.datos[actual][0]
                            self.datos[actual]=[]
                            self.elementos-=1
                            if(self.elementos==0):
                                self.vacia=True
                                self.inicio=0
                            self.llena=False
                            return dato
                            
                    else:
                        print("El elemento no está en la lista")
                else:
                    print("La lista está vacía")
                
                
        else:
            print("La lista está vacía")
    
    def mostrar(self):
        for i in self.datos:
            print(i)


prueba = listaLigada(2)

prueba.mostrar()