class Employee:
    position = "Software Engineer"
    salary = 70000
    department = "IT"

    def __init__(self, name, salary, position, department):
        self.name = name
        self.salary = salary
        self.position = position
        self.department = department

    def getinfo(self):
        print (f"{self.name}, {self.position}, {self.salary}, {self.department}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

Employee.greet()
Azzy = Employee("Azzy", 90000, "Data Scientist", "IT")

John = Employee("John", 80000, "Developer", "IT")

Glitch = Employee("Glitch", 100000, "Software Engineer", "HR")

Azzy.getinfo()
John.getinfo()
Glitch.getinfo()