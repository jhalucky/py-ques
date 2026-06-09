# Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.
# check if it is prime or not

# def is_prime(num):

#     primes= []

#     if num <= 1:
#         print("Not prime")
    
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not Prime")
#     print("Its prime")

    

# is_prime(20)

# print alternate prime numbers
list = [2,3,5,7,11,13,17,19]

print(list[::1])