# A class is a blueprint of an object
# Objects are instances of a class
class Person:
    name = "Joe"
    age = 34
    gender = "Male"

    def walk(self):
        print("Walking")

p=Person()
p.walk()

print(p.name)

