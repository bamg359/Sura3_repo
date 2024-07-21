from util.Conexion import Conexion


class Person_Type:

    id_type = None
    type = None

    def __init__(self, id_type, type):
        self._id_type = id_type
        self._type = type

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        self._id_type = id_type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    db.connect()


    @staticmethod
    def from_row(row):
        return Person_Type(row[0], row[1])

    def create_type_person(self, db):
        self._type = input("Ingrese P_NAT , si es persona Natural o P_JU si es persona juridica")
        query = "INSERT INTO costumer_type(costumer_type) VALUES(%s)"
        values = (self._type,)
        db.execute_query(query, values)


    def select_person_type(self, db):
        query = "SELECT * FROM costumer_type"
        result = db.execute_query(query)
        if result:
            types = []
            for row in result:
                type = Person_Type.from_row(row)
                types.append(type)
                #return types
                print(row[0], row[1])
        else:
            print("Tipo de personas No encontrada")
            return []






