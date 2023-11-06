class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
stud=student('jessa',14)
print('name:',stud.name,stud.get_age())
stud.set_age(16)
print('name:',stud.name,stud.get_age())