from domain.Category import Category
from domain.Product import Product
from util.Conexion import Conexion

db = Conexion(host = 'localhost', port = 3307 , user = 'root' , password= ""  , database= 'tienda_sura_g3')
db.connect()


category = Category(None, None)
product = Product(None, None, None, None, None, None, None, None, None)


category.create_category(db)
product.create_product(db)

