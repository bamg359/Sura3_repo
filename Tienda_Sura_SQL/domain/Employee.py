from domain.User import User
from util.Conexion import Conexion


class Employee(User):

    salary = None
    rol = None

    def __init__(self, user_id, name_user, last_name_user, email, password, salary, rol):
        super().__init__(user_id, name_user, last_name_user, email, password)
        self._salary = salary
        self._rol = rol

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    db.connect()

    @staticmethod
    def from_row_emp(row):
        return Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


    def create_user(self, db):
        super().create_user()
        self._salary = float(input("Ingrese valor del Salario Base del Empleado"))
        self._rol = int(input("Ingrese: \n 1. Gerente \n 2. Asesor \n 3. Cajero \n"))
        self.employee_insert(db)


    def employee_insert(self, db):
        query = "INSERT INTO employees (employee_id , employee_name , employee_last_name, email , emp_password, salary,rol) VALUES(%s, %s, %s, %s, %s , %s,%s)"
        values = (self._user_id, self._name_user, self._last_name_user, self._email, self._password, self._salary, self._rol)
        db.execute_query(query, values)

    def select_employees(self, db):
        query = "SELECT * FROM employees"
        result = db.execute_query(query)
        if result:
            employees = []
            for row in result:
                employee = Employee.from_row_emp(row)
                employees.append(employee)
                # return salarys
                print("Id: ", row[0],"\n", "Nombre: " + row[1]+"\n", "Apellido" + row[2]+"\n", "Correo"+ row[3]+"\n","Password: " +  row[4]+"\n","Salario",row[5],"\n","Rol: ", row[6] )
        else:
            print("empleados No encontrados")
            return []




    def find_employee_by_id(self, db):
        employee_id = int(input("Ingrese el id del empleado: "))
        query = "SELECT * FROM employees WHERE employee_id = %s"
        result = db.execute_query(query, (employee_id,))
        if result:
            return Employee.from_row_emp(result[0])
        else:
            print("empleado no encontrado")
            return None

    def select_employee_by_id(self, db):
        selected_employee = self.find_employee_by_id(db)
        if selected_employee:
            print("id: ", selected_employee._user_id)
            print("Nombre empleado: " , selected_employee._name_user)
            print("Apellido empleado: " , selected_employee._last_name_user)
            print("Correo del empleado: ", selected_employee._email)
            print("Salario: ", selected_employee._salary)
            print("Rol: ", selected_employee._rol)

    def update_employee(self, db):
        query = "UPDATE employees SET employee_id=%s, employee_name=%s,employee_last_name=%s, email=%s, emp_password=%s, salary =%s, rol= %s WHERE employee_id =%s"
        values = (self._user_id, self._name_user, self._last_name_user, self._email, self._password, self._salary, self._rol)
        db.execute_query(query, values)

    def delete_employee(self, db):
        employee_id = int(input("Indique el id del empleado a borrar: "))
        query = "DELETE FROM employees WHERE employee_id=%s"
        db.execute_query(query, (employee_id,))












