#list
#dictonary
#set
#generator

#list:-

#list1=["malayalam","abba","mom"]
#list2=[i for i in list1 if i == i[::-1]]                #pallindrome
#print(list2)


#list1=[1,2,3,4,5,6,7,8,9]
#list2=[i for i in list1 if i %2==0 ]
#list3=[i for i in list1 if i %2!=0 ]                    #even or odd
#print(list2)
#print(list3)

#demolist=[1,2,3,4,5]
#string="abc"
#list3=[(i,j) for i in demolist for j in string]         #value i and j
#print(demolist)                                            for i in demolist
#print(string)                                              for j in string
#print(list3)                                               print()



#set:-

#setdemo={1,2,3,4,5,6,7,8,9}
#set1={i**2 for i in setdemo}                                #multiplied
#print(set1)                                                     #its not ordered



#dictonary:-

#dict={i:i**2 for i in range(10)}
#print(dict)                                                    #multiplied values

#dictdemo={"anu":25,"abhi":30,"akhil":26}
#dict2={k.upper():v for (k,v)in dictdemo.items()}               #uppercase
#print(dict2)

#generator:-


input_list1=[1,2,3,4,5,6,7,8,9]
output_gen=(i for i in input_list1 if i%2==0)
for var in output_gen:                                          #list of even numbers
    print(var,end='')






