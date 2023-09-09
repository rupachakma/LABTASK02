list1=11

newlist=[]

for i in range(list1):
    i=int(input("Enter {} Digits: ".format(i)))
    newlist.append(i)

print("My Mobile Number is: ",newlist)

evenlist=[]
oddlist=[]

for i in  newlist:
    if i%2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("even list is:",evenlist)
print("odd list is:",oddlist)