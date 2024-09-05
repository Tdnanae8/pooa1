class Person():
    def __init__ (self,name,lastname):
        self.name = name
        self.lastname = lastname

    def change_color(self,color):
        self.eyescolor = color

    def say_hello(self):
        print(f"Hola mi nombre es {self.name} y mi apellido es {self.lastname}y mi color de ojos es {self.eyescolor}")

p1 = Person("Tiare","Baeza")
print(p1)
print(p1.name, p1.lastname)

p2 = Person("Romina","Pereira")
print(p2.name, p2.lastname)

p1.change_color("brown")
p2.change_color("green")

p1.say_hello()
p2.say_hello()