from domain.Costumer import Costumer
from domain.Person_Type import Person_Type
from util.Conexion import Conexion

db = Conexion(host = 'localhost', port = 3307 , user = 'root' , password= ""  , database= 'tienda_sura_g3')
db.connect()
type = Person_Type(None, None)
costumer = Costumer(None, None, None, None, None , None, None)

#type.create_type_person(db)
#costumer.create_user(db)

#type.select_person_type(db)
costumer.select_costumers(db)
costumer.select_costumer_by_id(db)