from View.View_Costumer import View_Costumer
from View.View_Employee import View_Employee
from domain.Costumer import Costumer
from domain.Person_Type import Person_Type
from util.Conexion import Conexion


class ViewSystem:

    def __init__(self, init):
        self.init = init



    costumer_manager = View_Costumer()
    employee_manager = View_Employee()


    def system_init(self):

        db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
        db.connect()

        self.init = int(input("Presione 1. para iniciar"))
        while self.init != 0:
            print("Presione 1. Para gestionar Clientes: \n 2. Para registrar Empleado \n 3. Para iniciar Sesion \n 4. Salir")
            select = int(input("Seleccione una opcion "))

            #Tambien se puede hacer con match que fue añadida en la version 3.10 de python , por estar usando la version 3.9 no puedo usarlo.
            if select == 1:
                print("Gestion de Clientes:")
                self.costumer_manager.menu_costumers(db)

            elif select == 2:
                print("Gestion de Empleados: ")
                self.employee_manager.menu_empleayee_manager(db)
            elif select == 3:
                print("Inicio sesion:")
            elif select == 4:
                print("Salir")
            else:
                print("Seleccione una opcion valida")







