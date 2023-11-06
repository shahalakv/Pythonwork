# file1=open("demofile.txt","w")
# file2=open("demofile1.txt","w")
# file1.write("sudhishma")
# file2.write("shahala")                                            #write
# file1.close()
# file2.close()


file=open("demofile.txt",'r')
#print(file.read())
#print(file.read(5))                                                #read
print(file.readline())
# print(file.readlines())
file.close()