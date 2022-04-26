class Parent():
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, childname):
       # super().__init__(childname)

c = Child("Bashir")
print(f'name in Parent class: {c.name}')