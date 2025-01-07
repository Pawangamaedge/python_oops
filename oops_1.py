class Person:
     def __init__(per, name, age = 30):
          per.user_name =  name
          per.user_age = age

     def display_name(per):
          print(f"good morning: {per.user_name}, your age is: {per.user_age}")


p = Person("sohan")
p.display_name()

