# try:
#     file1=open("demofi1e1.txt",'r')
#     cnt=file1.read()
#     print("demofile1",cnt)
#     file1.close()
# except FileNotFoundError:                                                       #FileNotFoundError
#     print("file not found")





# try:
#     n = int(input("enter number"))
#     list1=[1,3,4,5,6,7,8,9]                                                   #IndexError
#     v=list1[n]
#     print("index for list",v)
# except IndexError:
#     print("index doesnt exist")



# try:
#     name=input("enter the name")
#     print("the name is", name)
# except KeyboardInterrupt:                                                    #KeyboardInterrupt
#     print("its keyboardinterrupt error")


count=0
file=open("demofile1.txt",'r')
n=file.read().split()
for i in n:
    count=count+1
print("the no of words are:",count)
file.close()