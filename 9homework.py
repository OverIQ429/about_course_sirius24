class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def laptop_name(self):
        return print(self.brand + " " + self.model)

hp = Laptop('hp', '15-bw0xx', '57000')
print(hp.price)
print(hp.laptop_name())