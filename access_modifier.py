# this is public class example where we can access the public class members and function outside the child
# class as well using super() keyword 

class Public_class:
     def __init__(self, name, age):
          self.person_name = name
          self.person_age = age
          print("this is public class: ")

     def display_info(self):
          print(f"your name is: {self.person_name}")
          print(f"your age is: {self.person_age}")

# p = Public_class("ajay", 30)
# p.display_info()

class Extended_public_class(Public_class):
     def __init__(self, name, age, salary, location, department):
          super().__init__(name, age)
          self.person_salary = salary
          self.person_location = location
          self.person_department = department

     def display_info(self):
          super().display_info()
          print(f"your salary is: {self.person_salary}")
          print(f"your location is: {self.person_location}")
          print(f"your department is: {self.person_department}")

# ep = Extended_public_class('ajay', 40, 30000,'indore', 'it_department')
# ep.display_info()



# private class example where can access the data member within inside the class, 
# we can also access it in child class and outsidee the class using setter and getter methods
class Private_class:
     def __init__(self, name, age):
          self.__person_name = name
          self.__person_age = age
          print("this is private class: ")

     def get_name(self):
          return self.__person_name

     def get_name_1(self):
          print(f"person_name: {self.__person_name}")

     def get_age(self):
          return self.__person_age
     
     def get_age_1(self):
          print(f"person_age: {self.__person_age}")

     def display_info(self):
          print(f"your name is: {self.__person_name}")
          print(f"your age is: {self.__person_age}")

class Extended_private_class(Private_class):
     def __init__(self, name, age, salary, location, department):
          super().__init__(name, age)
          self.__person_salary = salary
          self.__person_location = location
          self.__person_department = department

     def person_display_name(self):
          super().get_name_1()

     def person_display_age(self):
          super().get_age_1()

     def display_info(self):
          super().display_info()
          print(f"your salary is: {self.__person_salary}")
          print(f"your location is: {self.__person_location}")
          print(f"your department is: {self.__person_department}")

# ep_private = Extended_private_class('ajay', 40, 30000,'indore', 'it_department')
# ep_private.display_info()
# ep_private.person_display_name()
# ep_private.person_display_age()
# print(f"name: {ep_private.__person_name}") # thiss will give error




class Protected_class:
     def __init__(self, name, age):
          self._person_name = name
          self._person_age = age
          print("this is protected class: ")

     def get_name(self):
          return self._person_name

     def _get_name_1(self):
          print(f"person_name: {self._person_name}")

     def get_age(self):
          return self._person_age
     
     def _get_age_1(self):
          print(f"person_age: {self._person_age}")

     def display_info(self):
          print(f"your name is: {self._person_name}")
          print(f"your age is: {self._person_age}")

class Extended_protected_class(Protected_class):
     def __init__(self, name, age, salary, location, department):
          super().__init__(name, age)
          self._person_salary = salary
          self._person_location = location
          self._person_department = department

     def person_display_name(self):
          super()._get_name_1()

     def person_display_age(self):
          super()._get_age_1()

     def display_info(self):
          super().display_info()
          print(f"your salary is: {self._person_salary}")
          print(f"your location is: {self._person_location}")
          print(f"your department is: {self._person_department}")

ep_protected = Extended_protected_class('ajay', 40, 30000,'indore', 'it_department')
ep_protected.display_info()
ep_protected.person_display_name()
ep_protected.person_display_age()
print(f"name: {ep_protected._person_name}")

