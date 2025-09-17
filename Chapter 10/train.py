
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro_m, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro_m} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro_m, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro_m}\
 to {to} is {randint(222, 5555)}")  


t = Train(2917)
t.book("Lahore", "Rawalpindi")
t.getStatus()
t.getFare("Lahore", "Rawalpindi")
