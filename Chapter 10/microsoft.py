class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(self.name, self.salary, self.pin, self.company)


p = Programmer("Azzy", 1200000, 245001)
r = Programmer("Jazzy", 1000000, 245001)