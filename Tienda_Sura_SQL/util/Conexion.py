

import mysql.connector


class Conexion:


    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    _instance = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(

                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conexion Exitosa a la base de datos")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos")


    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión Cerrada")

    def execute_query(self, query, params = None):
        cursor = self.connection.cursor(buffered = True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta Ejecutada de manera exitosa")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta")
            return None
        finally:
            cursor.close()

    """"
    def __new__(cls):
        if cls._instance is None:
                cls._instance = super(Conexion, cls).__new__(cls)
                try:
                    cls._instance.connection = mysql.connector.connect(host='localhost', port=3306, user='root', password="", database='tienda_sura_g3')
                    cls._instance.cursor()
                    cursor = cls._instance.connection.
                except  
                
    """
