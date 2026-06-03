# string reversal
# str = "Python"

# print(str[::-1])

# count no of vowels in a sentence

# vowels = 'aeiou'

# str = "Priyanshi study hard and get a job and start feeding me"

# counter = 0

# for i in str.lower():
#     if i in vowels:
#         counter += 1 

# print(counter)

# findin min/max in a list

# lst = [45, 69, 72, 8, 0, 29]

# print(max(lst), min(lst))

# removing duplicates

# data = [1, 2, 2, 3, 4, 4, 4, 5]

# unique_lst = list(set(data))

# print(unique_lst)



# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 70, 76, 10, 24]

# for i in numbers_x:
#     if i[0] == i[-1]:
#       print("result is True")

#     else:
#        print("False")


def first_last_same(number_list):

    if number_list[0] == number_list[-1]:
        return True
    else:
        return False
    


numbers_x = ['10','20','30','40','10']
print("result is", first_last_same(numbers_x))