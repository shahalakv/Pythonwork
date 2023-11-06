#def sum1(a,b):
 #   s=a+b
  #  print(s)                                           #sum
#sum1(20,60)


#def tr(l,b):
 #   area=l*b                                           #area of triangle
  #  print(area)
#tr(5,6)


#def sum1(n):
 #   if n>0:
  #      return n + sum1(n-1)                           #recursion
   # else:                                               #sum of n natural numbers
    #    return 0
#print(sum1(5))


#add=lambda x,y:print(x*y)                              #add lambda
#add(15,15)


num = [1,2,3,4,5,6,7,8,9]
print("original list:")
print(num)
print("\n even number list:")
even_num = list(filter(lambda x:x%2==0,num))            #odd and even
print(even_num)                                         #lambda using filter
print("\n odd number list:")
odd_num = list(filter(lambda x:x%2!=0,num))
print(odd_num)



