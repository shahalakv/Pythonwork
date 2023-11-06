class vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def info(self):
        print(self.name,self.color,self.price)
class car(vehicle):
    def change_gear(self,no):
        print(self.name,'change gear no',no)
car=car('toyoto','black',35000000)
car.info()
car.change_gear(5)