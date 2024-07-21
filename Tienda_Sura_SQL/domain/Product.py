



class Product:

    def __init__(self, product_id, product_name , description, cost , price, quantity , state):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._cost = cost
        self._price = price
        self._quantity = quantity
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
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

