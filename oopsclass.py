class employee:
    employeetype="government"
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def show(self):
        print("the employee details are",self.id,self.name,self.salary)
print(employee.employeetype)
e1=employee(1,'shahala',30000)
e1.show()

