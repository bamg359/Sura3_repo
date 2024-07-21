from util.Conexion import Conexion


class Rol:
    def __init__(self, id_rol, rol):
        self._id_rol = id_rol
        self._rol = rol

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    db = Conexion(host='localhost', port=3307, user='root', password="", database='tienda_sura_g3')
    db.connect()


    @staticmethod
    def from_row_rol(row):
        return Rol(row[0], row[1])

    def create_rol(self, db):
        self._rol = input("Ingrese: \n Gerente \n Asesor \n Cajero \n")
        query = "INSERT INTO rol(rol_name) VALUES(%s)"
        values = (self._rol,)
        db.execute_query(query, values)


    def select_rol(self, db):
        query = "SELECT * FROM rol"
        result = db.execute_query(query)
        if result:
            rols = []
            for row in result:
                rol = Rol.from_row_rol(row)
                rols.append(rol)
                #return rols
                print(row[0], row[1])
        else:
            print("Rol No encontrado")
            return []