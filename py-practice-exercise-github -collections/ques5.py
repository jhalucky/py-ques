def str_slicing():

    str = input("Enter the string: ")
    n = int(input("Enter the index: "))
    print(str[n::]) #it will print substring from index n to end
    print(str[n::2]) #it will extract substring on a step size of 2
    print(str[n:5]) #it will also extract string from nto 5
    


str_slicing()
