number=int(input("enter the number"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is an prime number")
        
else:
    print(number,"is not a prime number")
