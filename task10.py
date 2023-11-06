# class vehicle:
#     def __init__(self,speed,mileage):
#         self.speed=speed
#         self.mileage=mileage
#     def show(self):
#         print('hi,vehicle',self.speed,self.mileage)
# s1=vehicle(200,15)
# s1.show()



# class vehicle:
#     pass
# s1=vehicle()


class employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def detail(self):
        print(self.name,self.age)
class department(employee):
    pass

dep=department('shahala',24)
dep.detail()




# psum=0
# for i in range(1,11):
#     sum1=psum+i
#     print('current',i,'psum',psum,'is',sum1)
#     psum=i

