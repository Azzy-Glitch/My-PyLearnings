class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):
    company = "Infotech"
    def showLanguage(self):
        print(f"The name of programmer is {self.name} and He is good\
 with {self.language} language")


b = Programmer()
b.show()
b.printLanguages()
b.showLanguage()