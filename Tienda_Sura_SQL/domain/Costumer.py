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

    db = Conexion(host='localhost', port=3306, user='root', password="", database='tienda_sura_g3')
    db.connect()


    def create_costumer(self):
        self._user_id = int(input("Ingrese el id del clinte"))


    def costumer_insert(self, db):
        query = "INSERT INTO costumer (costumer_id , costumer_name , costumer_last_name, email , cost_password, costumer_type,points) VALUES(%s, %s, %s, %s, %s , %s,%s)"
        values = (self._user_id, self._name_user, self._last_name_user, self._email, self._password, self._type, self._points)
        db.execute_query(query, values)


