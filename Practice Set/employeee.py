class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = 0
        self.salary = salary   # uses setter

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("Salary must be greater than 0")
        self._salary = value

    def display_info(self):
        return f"Employee: {self._name}, Salary: {self._salary}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # inheritance
        self._bonus = 0
        self.bonus = bonus  # uses setter

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError("Bonus cannot be negative")
        self._bonus = value

    # Method overriding
    def display_info(self):
        return f"Manager: {self._name}, Salary: {self._salary}, Bonus: {self._bonus}"

    # Bonus method
    def total_compensation(self):
        return self._salary + self._bonus
    
emp = Employee("Ali", 50000)
print(emp.display_info())

emp.salary = 60000
print(f"Salary increased to {emp.salary}")

# # emp.salary = -1000  # This will raise a ValueError due to validation in the setter

mgr = Manager("Azzy", 80000, 20000)
print(mgr.display_info())

mgr.salary = 85000
print(f"Salary increased to {mgr.salary}")

mgr.bonus = 30000
print(f"Bonus increased to {mgr.bonus}")

print(f"Total compensation: {mgr.total_compensation()}")