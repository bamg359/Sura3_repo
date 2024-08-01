

from fastapi import FastAPI, Body

from fastapi.responses import HTMLResponse

from tienda.Conexion import Conexion

app = FastAPI()

db = Conexion(host='localhost', port=3306, user='root', password="", database='tienda_sura_2')

db.connnect_db()

class Product():


    def __init__(self, product_id, product_name, description, category,  price, quantity, brand):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._category = category
        self._price = price
        self._quantity = quantity
        self._brand = brand

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @staticmethod
    def from_row(row):
        return Product(row[0], row[1],row[2], row[3], row[4], row[5], row[6])


    @app.post('/create_product/{product_id, product_name, decription, category, price, quantity, brand}' , tags= ["Crear producto"])
    def create_product(product_id:int = Body(),product_name: str = Body(), description: str = Body(), category: int = Body(), price: float = Body(), quantity: int = Body(), brand:str = Body()):
        query = "INSERT INTO product ( product_id , product_name , description, category, price, quantity, brand) VALUES( %s,%s, %s, %s, %s, %s, %s) "
        values = (product_id, product_name, description, category, price, quantity, brand)
        db.execute_query(query, values)

    @staticmethod
    @app.get('/select_products/', tags=["Consultar productos"])
    def select_products():
        query = "SELECT * FROM product"
        result = db.execute_query(query)
        if result:
            products = []
            for row in result:
                product = Product.from_row(row)
                products.append(product)
                #print(row[0], row[1],row[2], row[3], row[4], row[5] , row[6])
            return products
        else:
            print("Productos no encontradas")
            return []


    @app.delete('/delete_product/{product_id}', tags = ["Eliminar Producto"])
    def delete_product(product_id :int):
        query = "DELETE FROM product WHERE product_id = %s"
        db.execute_query(query, (product_id,))

    @app.put('/update_product/{product_id, product_name, decription, category, price, quantity, brand}' , tags= ["Actualizar producto"])
    def update_product(product_id:int = Body(),product_name: str = Body(), description: str = Body(), category: int = Body(), price: float = Body(), quantity: int = Body(), brand:str = Body()):
        query = "UPDATE product SET  product_name = %s, description = %s, category = %s, price = %s, quantity = %s, brand = %s WHERE product_id = %s"
        values = (product_name, description, category, price, quantity, brand, product_id)
        db.execute_query(query, values)

