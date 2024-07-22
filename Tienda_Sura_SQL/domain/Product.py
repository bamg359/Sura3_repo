



class Product:

    def __init__(self, product_id, product_name , description, cost , profit, price, quantity , category, state):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._cost = cost
        self._profit = profit
        self._price = price
        self._quantity = quantity
        self._category = category
        self._state = state


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
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def profit(self):
        return self._profit

    @profit.setter
    def cost(self, profit):
        self._profit = profit

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
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state



    def create_product(self, db):
        self._product_id = int(input("Ingrese el id del producto"))
        self._product_name = input("Ingrese el nombre del producto")
        self._description = input("Ingrese la descripción del producto")
        self._category = int(input("Ingrese la categoria "))
        self._cost = float(input("Ingrese el costo del producto"))
        self._profit = float(input("Ingrese el margen de ganancia desea para el producto"))
        self._price = self._cost/(1- (self._profit/100))
        self._quantity = int(input("Ingrese la cantidad de producto"))
        print("Seleccione 1 para dejar el estado del producto como disponible , 0 para no disponible")
        self._state = self.create_state()
        self.product_insert(db)

    def product_insert(self, db):
        query = "INSERT INTO product (product_id , product_name , description, category, cost , profit, price, quantity  , state) VALUES(%s,%s,%s, %s, %s, %s, %s , %s,%s)"
        values = (self._product_id, self._product_name, self._description, self._category, self._cost, self._profit, self._price, self._quantity, self._state)
        db.execute_query(query, values)


    def create_state(self):
        select = int(input("Selecciona 1 Para activo , 0 para inactivo"))
        active="Disponible"
        inactive="No Disponible"

        if select == 1:
            return active
        else:
            return inactive




