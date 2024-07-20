


class User:


    user_id = None
    name_user = None
    last_name_user = None
    email = None
    password = None


    # comment

    def __init__(self, user_id, name_user, last_name_user, email, password):
        self._user_id = user_id
        self._name_user = name_user
        self._last_name_user = last_name_user
        self._email = email
        self._password = password


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id


    def create_user(self):
        self._user_id = int(input("Ingrese el id del usuario"))
        self._name_user = input("Ingrese el nombre del usuario")
        self._last_name_user = input("Ingrese el apellido del usuario")
        self._email = input("Ingrese el correo del usuario")
        self._password = input("Ingrese la contraseña")


