#amstrong
a=int(input("enter the number:"))
sum=0
temp=a
while temp > 0:
    digit =temp%10
    sum+=digit**3
    temp//=10                                       #amstrong
if a==sum:
    print(a,"is an amstrong")
else:
    print(a,"is not amstrong")