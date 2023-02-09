# Check the number you input whether its prime or not. 

number = int(input("Input a number"))
if number > 1:

    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")
    
    
    
    
# Input: 
# Input a number 4

# Output:
# 4 is not a prime number
