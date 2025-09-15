class Employee:
    position = "Software Engineer"
    salary = 70000
    department = "IT"

    def getinfo(self):
        print (f"{self.name}, {self.position}, {self.salary}, {self.department}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

Employee.greet()
Azzy = Employee()
Azzy.name = "Azzy"
Azzy.position = "Data Scientist"  # Instance attribute overriding class attribute
# print(Azzy.position)

John = Employee()
John.name = "John"
John.salary = 80000  # Instance attribute overriding class attribute
# print(John.salary)

Glitch = Employee()
Glitch.name = "Glitch"
Glitch.salary = 100000
Glitch.department = "HR"  # Instance attribute overriding class attribute
# print(Glitch.department)

# Employee.getinfo(Azzy)
# Employee.getinfo(John)
# Employee.getinfo(Glitch)

Azzy.getinfo()
John.getinfo()
Glitch.getinfo()