# from model import PersonajesModel
# from view import PersonajesView

# class PersonajesController:
#     def __init__(self):
#         self.modelo = PersonajesModel()
#         self.view = PersonajesView()
#         print(self.view)
#         print(self.modelo)

#     def get_user_details(self):
#         nombre = input("Introduce un nombre: ")
#         email = input("Introduce un email: ")
#         self.modelo = PersonajesModel(nombre, email)

#     def show_user_details(self):
#         self.view.show_user_details(self.modelo)


from model import UserModel
from view import UserView

class UserController:
    def __init__(self):
        self.model = UserModel("", "")
        self.view = UserView()

    def get_user_details(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        self.model = UserModel(name, email)

    def show_user_details(self):
        self.view.show_user_details(self.model)
