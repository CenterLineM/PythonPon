__author__ = 'Administrator'
class Worker:
    def  int(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob =  Worker('Bob Smith' , 50000)
sue =  Worker('Sue Jones',  60000)
bob.lastName()
sue.lastName()
sue.giveRaise(.10)
sue.pay