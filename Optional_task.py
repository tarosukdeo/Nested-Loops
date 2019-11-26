num = int(input("Enter  number:\n"))

if (num > 1):
    for x in range(2, num):
        if (num % x == 0):
            print("%d is not a prime number!" %num)
            break
        
    else:
        print("%d is a prime number!" %num)

else:
    print("You didn't enter a number greater than 1!")
