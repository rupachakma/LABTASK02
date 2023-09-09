list1=11
newlist=[]

for i in range(list1):
    i=int(input("Enter {} Digits: ".format(i)))
    newlist.append(i)

print("Before Sorting:",newlist)

for i in range(len(newlist)):
    for j in range(0,len(newlist)-1):
        if newlist[j] > newlist[j+1]:
            temp = newlist[j]
            newlist[j] = newlist[j+1]
            newlist[j+1] = temp

print("After Sorting:",newlist)

