class Employee:
    position = "Software Engineer"
    salary = 70000
    department = "IT"

Azzy = Employee()
Azzy.name = "Azzy"
print(Azzy.name, Azzy.position, Azzy.salary, Azzy.department)

John = Employee()
John.name = "John"
John.salary = 80000  # Instance attribute overriding class attribute
print(John.name, John.position, John.salary, John.department)

Glitch = Employee()
Glitch.name = "Glitch"
Glitch.department = "HR"  # Instance attribute overriding class attribute
print(Glitch.name, Glitch.position, Glitch.salary, Glitch.department)