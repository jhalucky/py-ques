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

# fib(10)

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

fibonacci(5)
