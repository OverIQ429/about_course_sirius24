class Company:
    def __init__(self, balance = 0):
        self.director = None
        self.employers = []
        self.profite = balance

    def set_profit(self, profite):
        self.profite += profite

    def create_director(self, first_name, second_name, Id, salary):
        self.director = Director(first_name, second_name, Id, salary)
        self.employers.append(self.director)

    def create_employee(self, first_name, second_name, Id, salary):
        employer= Employer(first_name, second_name, Id, salary)
        self.employers.append(employer)

    def fulfill_promise(self):
        for employer in self.employers:
            if self.profite > 0:
                employer.get_paid(True)
                self.profite -= employer.salary
            else:
                employer.get_paid(False)

    def get_director(self):
        return self.director


class Director:
    def __init__(self, first_name, second_name, Id, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.id = Id
        self.salary = salary
        self.promises = []

    def get_paid(self, profite):
        self.promises.append(profite)

    def check_promises(self):
        print(self.promises[-1])

class Employer:
    def __init__(self, first_name, second_name, Id, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.id = Id
        self.salary = salary
        self.promises = []

    def get_paid(self, profite):
        self.promises.append(profite)

    def check_promises(self):
        print(self.promises[-1])

vk = Company(balance=50)
vk.create_director(
    first_name = "Владимир",
    second_name = "Кириенко",
    Id = 1,
    salary = 15
    )

vk.create_employee(
    first_name = "Елена",
    second_name = "Иванова",
    Id = 2,
    salary = 8
    )

vk.create_employee(
    first_name = "Виктор",
    second_name = "Кузнецов",
    Id = 3,
    salary = 6
    )

vk.set_profit(145.12)
vk.fulfill_promise()

director = vk.director
director.check_promises() # true

vk.set_profit(-200)
vk.fulfill_promise()

director.check_promises() # false