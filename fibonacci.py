# def fib(n):

#     a = 0
#     b = 1

#     if n == 1:
#         print(1)

#     else:
#         print(a)
#         print(b)

#         for i in range(n):
#             c = a + b
#             a = b
#             b = c
#             print(c)

# fib(15)

def fibonacci(n):
    a,b = 0,1

    if n == 1:
        print(a)

    else:

        print(a,end=' ')
        print(b,end=' ')
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c,end=' ')

fibonacci(15)

# n = int(input("Enter a num: "))
# fact = 1

# for i in range(1,6):
#     while i < 6:
#         fact*=i
#         i+=1

# print(fact)


# import random 

# n = random.randint(1,100)
# guess = int(input("Enter number: "))

# counter = 1
# while guess != n:
#     if guess < n:
#         print("Guess higher")
#     else:
#         print("Guess lower")

#     guess = int(input("Enter number again: "))
#     counter += 1

# else:
#     print("You guessed right in",counter,"attempts")

# n = int(input("Enter the number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(fact)

# i = 1
# n = int(input("Enter the number of terms: "))

# while i <=n:
#     print("*" * i)
#     i += 1