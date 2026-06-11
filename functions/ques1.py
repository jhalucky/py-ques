def is_even(num):

    """this function checks whether the number is even or not"""
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
        
    else:
        return 'Abe chutiye!'
    
print(is_even('hello'))
    

n = int(input("Enter any number: "))
for i in range(1,n):
    print(i, is_even(i))


# how to access doc string of any function

print(is_even.__doc__)

# using __doc__ we can access any function's documentation
