class Array():
    def __init__( self, tamano ):
        self.__tamano = tamano
        self.__data = [1 for x in range(self.__tamano)]

    def get_item( self, index ):
        return self.__data[ index ]

    def to_string( self ):
        print( self.__data )

    def clear ( self, dato ):
        self.__data = [dato for x in range(self.__tamano)]

    def getLenght( self ):
        return self.__tamano
    
    def setItem( self, index, dato ):
        self.__data[ index ] = dato

class Trabajador:
    def __init__( self , nt , nom , pat , mat , h_extra , sueldo , anio_ingreso):
        self.num_trabajador = nt
        self.nombre = nom
        self.paterno = pat
        self.materno = mat
        self.horas_extra = h_extra
        self.sueldo = sueldo
        self.anio_ingreso = anio_ingreso
    
    def set_num_trabajador( self , nt):
        self.num_trabajador = nt

    def get_num_trabajador( self ):
        return int( self.num_trabajador )

    def set_nombre( self , nom):
        self.nombre = nom

    def get_nombre( self ):
        return self.nombre

    def set_paterno( self , pat):
        self.paterno = pat

    def get_paterno( self ):
        return self.paterno

    def set_materno( self , mat):
        self.materno = mat

    def get_materno( self ):
        return self.materno

    def set_h_extra( self , h_extra):
        self.horas_extra = h_extra

    def get_h_extra( self ):
        return int( self.horas_extra )

    def set_sueldo( self , sueldo):
        self.sueldo = sueldo

    def get_sueldo( self ):
        return int( self.sueldo )

    def set_anio_ingreso( self , anio_ingreso):
        self.anio_ingreso = anio_ingreso

    def get_anio_ingreso( self ):
        return int( self.anio_ingreso )

    def antiguedad( self ):
        return 2021 - int( self.anio_ingreso )

class Empresa:

    def __init__( self ):
        # codigo para leer el archivo, podria ser un metodo local
        txt = open( 'junio.dat', 'r' )                 
        info = txt.readlines()

        for index in range( len(info) ):
            info[index] = info[index].rstrip('\n').split(',')

        self.info = info 
        self.empleados = Array(15)
        # codigo para crear un objeto por cada linea leida del archivo y meterlo al array.
        contador = 0
        for i in ( self.info ):
            emp = Trabajador( i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            # print(emp)            
            self.empleados.setItem( contador, emp )
            # print( self.empleados.get_item(contador) )
            contador += 1
            # print(contador)

    def get_info(self):
        return self.info    

    def get_empleado( self, numE ):
        return self.empleados.get_item(numE)  

    # def get_empleados( self ):
        # return self.empleados.to_string()

    def calcular_sueldos( self ):
        # codigo para recorrer self.empleados y mostrar lo que se pide los sueldos con las reglas
        for i in range( self.empleados.getLenght() - 1):
            emp = self.get_empleado( i + 1 )

            extra = emp.get_h_extra() * 80
            # print(extra)
            suma = emp.get_sueldo() + extra
            # emp.set_sueldo( suma )
            print(suma)


    def encontrar_mayor_ant( self ):
        # codigo para calcular al mas antiguo y mostrarlo en pantalla
        masAntiguo = 0
        nomEmpleado = ''
        nomEmpleados = ''

        for i in range( self.empleados.getLenght() - 1):
            # print( i )
            emp = self.get_empleado( i + 1)
            # print( emp )
            if emp.antiguedad() > masAntiguo:
                masAntiguo = emp.antiguedad()
                nomEmpleado = emp.get_nombre()
                # print(nomEmpleado)
                nomEmpleados = nomEmpleado
            elif emp.antiguedad() == masAntiguo:
                nomEmpleado = emp.get_nombre()
                # print(nomEmpleado)
                nomEmpleados = nomEmpleados + ' ' + nomEmpleado
        # print(masAntiguo)
        # print(nomEmpleado)
        return nomEmpleados

        

# ejemplo = Array(5)

# ejemplo.to_string()
# print(ejemplo.get_item(3))
# ejemplo.clear(2)
# ejemplo.to_string()
# print(ejemplo.getLenght())
# ejemplo.setItem( 3, 2 )
# ejemplo.to_string()

# lista = Array(10)

# lista.setItem( 0, 33)
# lista.setItem( 1, 3)
# lista.setItem( 2, 88)
# lista.setItem( 3, 42)
# lista.setItem( 4, 12)
# lista.setItem( 5, 28)
# lista.setItem( 6, 14)
# lista.setItem( 7, 100)
# lista.setItem( 8, 1)
# lista.setItem( 9, 60)

# for i in range(lista.getLenght()):
#     print(lista.get_item(i))



txt = open('junio.dat','rt')
info = txt.readlines()

for index in range( len(info) ):
    info[index] = info[index].rstrip('\n').split(',')

print(info)

# novelFractal = Empresa()

# print(novelFractal.encontrar_mayor_ant())
# novelFractal.calcular_sueldos()

# emp1 = novelFractal.get_empleado( 1 )

# print( emp1.get_sueldo() )