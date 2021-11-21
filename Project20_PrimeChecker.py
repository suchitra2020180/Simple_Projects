###Project 20: prime number checker
## Prime number is divisible by 1 and itself.
def prime_checker(number):
    prime_identified=True
    for i in range(2,number):
        if number%i==0:
            #print("It's not a prime number")
            prime_identified=False
    if prime_identified==False:
        print("It's not a prime number")
    else:
        print("It's a prime number")
        



num=int(input("Enter a number to check if the number is prime or not: "))
prime_checker(num)