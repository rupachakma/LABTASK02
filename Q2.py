# list1=int(input("Enter Your Mobile Number :"))
list1=11

newlist=[]

for i in range(list1):
    i=int(input("Enter {} Digits: ".format(i)))
    newlist.append(i)

print("My Mobile Number is: ",newlist)


def max_value(n):
    max_value=n[0]
    for i in n:
        if i > max_value:
            max_value=i
    return max_value


print("max number in newlist is: ", max_value(newlist))

def min_value(y):
    min_value=y[0]
    for i in y:
        if i < min_value:
            min_value=i
    return min_value

print("Min number in newlist is :",min_value(newlist))

