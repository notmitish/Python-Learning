class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("Hello "+ self.name)
    
    def get_age(self):
        print("You are " + str(self.age) + " years old")
    
p1 = Person("Ashmit", 16)
p1.get_name()
p1.get_age()    