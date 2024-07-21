from domain.Costumer import Costumer
from domain.Person_Type import Person_Type
from util.Conexion import Conexion


class ViewSystem:

    def __init__(self, init):
        self.init = init

    db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    db.connect()
    type = Person_Type(None, None)
    costumer = Costumer(None, None, None, None, None, None, None)


    def system_init(self):
        self.init = int(input("Presione 1. para iniciar"))
        while self.init != 0:
            print("Presione 1. para registrar Cliente: \n 2. Para registrar Empleado \n 3. Para iniciar Sesion \n 4. Salir")
            select = int(input("Seleccione una opcion "))

            #Tambien se puede hacer con match que fue añadida en la version 3.10 de python , por estar usando la version 3.9 no puedo usarlo.
            if select == 1:
                print("Creación Clientes:")

            elif select == 2:
                print("Registro Empleado: ")
            elif select == 3:
                print("Inicio sesion:")
            elif select == 4:
                print("Salir")
            else:
                print("Seleccione una opcion valida")


    def menu_clientes(self, db):
        print("1. Crear tipo Cliente")
        print("2. Crear Cliente")
        print("3. Consultar Listado de Clientes")
        print("4. Consultar Cliente por Id")
        print("5. Actualizar Cliente")
        print("6. Eliminar Cliente")

        select = int(input("Seleccione una opción"))

        if select == 1:
            print("Crear tipo Cliente:")
            self.menu_person_type(db)
        elif select == 2:
            print("Registrar Cliente: ")
        elif select == 3:
            print("Consultar listado de clientes")
        elif select == 4:
            print("Consultar cliente por Id: ")
        elif select == 5:
            print("Actualizar cliente: ")
        elif select == 6:
            print("Eliminar cliente: ")
        else:
            print("Seleccione una opcion valida")

    def menu_person_type(self, db):
        print("1. Crear Tipo de Persona")
        print("2. Lista tipo de persona")
        select = int(input("Seleccione una opción"))
        if select == 1:
            print("Crear tipo Cliente: ")
            self.type.create_type_person(db)
        elif select == 2:
            print("Listar tipos de persona: ")
            self.type.select_person_type(db)
        else:
            print("Seleccione una opcion Valida")




