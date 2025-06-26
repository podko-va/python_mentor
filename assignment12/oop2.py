# class User:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f"User: {self.name} {self.surname}"
#
#
# user = User("Майкл", "Смит")
# # str() __str__
# user > 1


# class User:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def get_name(self):
#         return self.name
#
#     def get_fullname(self):
#         return f"{self.name} {self.surname}"
#
#     def set_name(self, new_name):
#         if isinstance(new_name, str):
#             self.name = new_name
#
# user = User("Майкл", "Смит")
#
# print(user.get_fullname())


# class User:
#     def __init__(self, name, surname):
#         self._name = name
#         self.surname = surname
#
#     @property
#     def name(self):
#         return self._name
#
#
# user = User("Майкл", "Смит")
#
# print(user.name)
# user.name = "Jack"

# class User:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     def get_name(self):
#         return self.__name
#
#
# user = User("Майкл", "Смит")
# print(user.get_name())


# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(self.name)
#
#
# class ProUser(User):
#     def greet(self):
#         print(f"***{self.name}***")
#
#
# class Admin(ProUser):
#     def greet(self):
#         print(f"Администратор {self.name}")
#
# user = User("Alex")
# user.greet()
#
# pro_user = ProUser("Jack")
# pro_user.greet()
#
# admin = Admin("Mike")
# admin.greet()


# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def greet(self):
#         print(self.name)
#
#
# class ProUser(User):
#     def __init__(self, name,  surname, age, desc):
#         super().__init__(name, surname, age)
#         self.desc = desc
#
#     def greet(self):
#         print(f"***{self.name}***")
#
#     def show_description(self):
#         print(self.desc)
#
#
# user = User("Alex", "Smith", 25)
# user.greet()
#
# pro_user = ProUser("Jack", "Кузнецов", 40, "Всем привет")
# pro_user.greet()
# pro_user.show_description()
















