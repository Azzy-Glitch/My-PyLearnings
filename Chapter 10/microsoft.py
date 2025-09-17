class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(self.name, self.salary, self.pin, self.company)


Azzy = Programmer("Azzy", 1200000, 245001)
Jazzy = Programmer("Jazzy", 1000000, 245001)