class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog is running!")

class Fish(Animal):
    def move(self):
        print("The fish is swimming!")

class Bird(Animal):
    def move(self):
        print("The bird is flying!")


# Polymorphism in action
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
