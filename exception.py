# x=10
# y=0
# try:
#     z=x/y
#     print(z)
# except Exception:
#     print("exception occured")
# except ZeroDivisionError:
#     print("zero error occured")



#     z=x
# except NameError:
#     print("name error occured")
# else:
#     print("no exception occured")
# finally:
#     print("final exception")



x=8
y=1                                                             #raise an error
z=1
if x<5:
    raise Exception("values of x is less than 5")
else:
    print(x)