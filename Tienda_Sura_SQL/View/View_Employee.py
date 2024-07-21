from domain.Employee import Employee
from domain.Rol import Rol


class View_Employee:


    rol = Rol(None, None)
    employee = Employee(None, None, None, None, None, None, None)
    
    def menu_empleayee_manager(self, db):
        print("1. Gestionar Rol")
        print("2. Crear empleado")
        print("3. Consultar Listado de empleados")
        print("4. Consultar empleado por Id")
        print("5. Actualizar empleado")
        print("6. Eliminar empleado")

        select = int(input("Seleccione una opción"))

        if select == 1:
            print("Gestionar rol empleado:")
            self.menu_rol_manager(db)
        elif select == 2:
            print("Registrar empleado: ")
            self.employee.create_user(db)
        elif select == 3:
            print("Consultar listado de empleados")
            self.employee.select_employees(db)
        elif select == 4:
            print("Consultar empleado por Id: ")
            self.employee.select_employee_by_id(db)
        elif select == 5:
            print("Actualizar empleado: ")
            self.employee.update_employee(db)
        elif select == 6:
            print("Eliminar empleado: ")
            self.employee.delete_employee(db)
        else:
            print("Seleccione una opcion valida")

    def menu_rol_manager(self, db):
        print("1. Crear rol")
        print("2. Lista roles empleados")
        select = int(input("Seleccione una opción"))
        if select == 1:
            print("Crear rol empleado: ")
            self.rol.create_rol(db)
        elif select == 2:
            print("Listar roles de emplados: ")
            self.rol.select_rol(db)
        else:
            print("Seleccione una opcion Valida")