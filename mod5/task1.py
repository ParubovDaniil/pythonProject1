class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

    def honk(self):
        print("Beep Beep!")
# Пример использования
car1 = Car("Toyota", "Corolla", 2020, "Silver")
car2 = Car("Honda", "Civic", 2018, "Red")

car1.display_info()
car1.honk()

car2.display_info()
car2.honk()