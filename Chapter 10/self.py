class Employee:
    position = "Software Engineer"
    salary = 70000
    department = "IT"

    def getinfo(self):
        print (f"{self.name}, {self.position}, {self.salary}, {self.department}")
    

Azzy = Employee()
Azzy.name = "Azzy"

John = Employee()
John.name = "John"
John.salary = 80000  # Instance attribute overriding class attribute

Glitch = Employee()
Glitch.name = "Glitch"
Glitch.salary = 100000
Glitch.department = "HR"  # Instance attribute overriding class attribute

# Employee.getinfo(Azzy)
# Employee.getinfo(John)
# Employee.getinfo(Glitch)

Azzy.getinfo()
John.getinfo()
Glitch.getinfo()