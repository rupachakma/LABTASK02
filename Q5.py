num=int(input("Enter a Number to check Prime: "))

def Prime(number):
    
        count=0
  
        if number % 2 ==0:
            count = 1
        if count == 0:
            print("Prime")
        else:
            print("Not Prime")

Prime(num)