def calculatesum(num1,num2):
    total=num1+num2
    return total
print("sum:",calculatesum(5,3))


#or                                                     #return


def calculatesum(num1,num2):
    total=num1+num2
    result=calculatesum(5,3)
    print(result)


