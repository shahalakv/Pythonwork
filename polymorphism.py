class vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print('details',self.name,self.color,self.price)
    def max_speed(self):
        print('car max_speed is 170')
    def change_gear(self):
        print('car change 5 gear')

class car(vehicle):
    def max_speed(self):
        print('car max_speed is 240')
    def change_gear(self):
        print('car change 7 gear')
car =car('car x1','red',20000)
car.show()
car.max_speed()
car.change_gear()

vehicle =vehicle('truck x1','white',75000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()