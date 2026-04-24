class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = 0
        self.salary = salary 

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
        super().__init__(name, salary)
        self._bonus = 0
        self.bonus = bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError("Bonus cannot be negative")
        self._bonus = value

    # Override
    def display_info(self):
        return f"Manager: {self._name}, Salary: {self._salary}, Bonus: {self._bonus}"

    # Bonus method
    def total_compensation(self):
        return self._salary + self._bonusclass 
   
    def __init__(self, name, salary):
        self._name = name
        self._salary = 0
        self.salary = salary 

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
        super().__init__(name, salary)
        self._bonus = 0
        self.bonus = bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value < 0:
            raise ValueError("Bonus cannot be negative")
        self._bonus = value

    # Override
    def display_info(self):
        return f"Manager: {self._name}, Salary: {self._salary}, Bonus: {self._bonus}"

    # Bonus method
    def total_compensation(self):
        return self._salary + self._bonus