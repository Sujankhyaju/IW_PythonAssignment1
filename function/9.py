# Write a Python function that takes a number as a parameter and check the number is prime or not.

def check_prime(num):
    
    if num == 2:
        result =1
    
    else:
        for i in range(2,num):
            if num%i == 0 :
                result = 0
                break
            else:
                result = 1

        
    return "not Prime Number" if result==0 else "prime"




num = int(input("Enter a number::"))

print(check_prime(num))
