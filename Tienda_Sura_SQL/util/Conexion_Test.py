
from Conexion import Conexion


db = Conexion(host = 'localhost', port = 3307 , user = 'root' , password= ""  , database= 'tienda_sura_g3')
db.connect()