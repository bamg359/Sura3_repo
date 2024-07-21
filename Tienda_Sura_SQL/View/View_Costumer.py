from domain.Costumer import Costumer
from domain.Person_Type import Person_Type


class View_Costumer:

    type = Person_Type(None, None)
    costumer = Costumer(None, None, None, None, None, None, None)


    def menu_costumers(self, db):
        print("1. Gestión tipo Clientes")
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
            self.costumer.create_user(db)
        elif select == 3:
            print("Consultar listado de clientes")
            self.costumer.select_costumers(db)
        elif select == 4:
            print("Consultar cliente por Id: ")
            self.costumer.select_costumer_by_id(db)
        elif select == 5:
            print("Actualizar cliente: ")
            self.costumer.update_costumer(db)
        elif select == 6:
            print("Eliminar cliente: ")
            self.costumer.delete_costumer(db)
        else:
            print("Seleccione una opcion valida")

    def menu_person_type(self, db):
        print("1. Crear Tipo de Persona")
        print("2. Listar tipos de persona")
        select = int(input("Seleccione una opción"))
        if select == 1:
            print("Crear tipo persona: ")
            self.type.create_type_person(db)
        elif select == 2:
            print("Listar tipos de persona: ")
            self.type.select_person_type(db)
        else:
            print("Seleccione una opcion Valida")

