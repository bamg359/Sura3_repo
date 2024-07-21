from domain.User import User
from util.Conexion import Conexion


class Costumer(User):

    type = None
    points = None

    def __init__(self, user_id, name_user, last_name_user, email, password, type, points):
        super().__init__(user_id, name_user, last_name_user, email, password)
        self._type = type
        self._points = points

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points

    db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    db.connect()

    @staticmethod
    def from_row(row):
        return Costumer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])


    def create_user(self, db):
        super().create_user()
        self._type = int(input("Ingrese: \n 1. persona natural \n 2. Persona Juridica"))
        self._points = int(input("ingrese los puntos iniciales"))
        self.costumer_insert(db)


    def costumer_insert(self, db):
        query = "INSERT INTO costumers (costumer_id , costumer_name , costumer_last_name, email , cost_password, costumer_type,points) VALUES(%s, %s, %s, %s, %s , %s,%s)"
        values = (self._user_id, self._name_user, self._last_name_user, self._email, self._password, self._type, self._points)
        db.execute_query(query, values)

    def select_costumers(self, db):
        query = "SELECT * FROM costumers"
        result = db.execute_query(query)
        if result:
            costumers = []
            for row in result:
                costumer = Costumer.from_row(row)
                costumers.append(costumer)
                # return types
                print("Id: ", row[0],"\n", "Nombre: " + row[1]+"\n", "Apellido" + row[2]+"\n", "Correo"+ row[3]+"\n","Password: " +  row[4]+"\n","Tipo Usuario",row[5],"\n","Puntos: ", row[6] )
        else:
            print("Clientes No encontrados")
            return []




    def find_costumer_by_id(self, db):
        costumer_id = int(input("Ingrese el id del cliente: "))
        query = "SELECT * FROM costumers WHERE costumer_id = %s"
        result = db.execute_query(query, (costumer_id,))
        if result:
            return Costumer.from_row(result[0])
        else:
            print("Cliente no encontrado")
            return None

    def select_costumer_by_id(self, db):
        selected_costumer = self.find_costumer_by_id(db)
        if selected_costumer:
            print("id: ", selected_costumer._user_id)
            print("Nombre cliente: " , selected_costumer._name_user)
            print("Apellido Cliente: " , selected_costumer._last_name_user)
            print("Correo del cliente: ", selected_costumer._email)
            print("Tipo de cliente: ", selected_costumer._type)
            print("Puntos de cliente: ", selected_costumer._points)

    def update_costumer(self, db):
        query = "UPDATE costumers SET costumer_id=%s, costumer_name=%s,costumer_last_name=%s, email=%s, cost_password=%s, costumer_type =%s, points= %s WHERE costumer_id =%s"
        values = (self._user_id, self._name_user, self._last_name_user, self._email, self._password, self._type, self._points)
        db.execute_query(query, values)

    def delete_costumer(self, db):
        costumer_id = int(input("Indique el id del cliente a borrar: "))
        query = "DELETE FROM costumers WHERE costumer_id=%s"
        db.execute_query(query, (costumer_id,))












