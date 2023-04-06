class Person:
    def __init__(self, weight, color, height):
        self.weight = weight
        self.height = height
        self.color = color


person = Person(10, "black", 80)
print(person.weight)
