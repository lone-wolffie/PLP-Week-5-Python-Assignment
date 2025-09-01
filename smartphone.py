# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# Derived Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # inherits attributes from Smartphone
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} smoothly with {self.gpu} GPU!")

    # Polymorphism (overriding method)
    def info(self):
        print(f"Gaming Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, GPU: {self.gpu}")


# Create Objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 8", 512, "Adreno 740")

phone1.info()
phone1.call("0722334455")

phone2.info()
phone2.play_game("Call of Duty")
