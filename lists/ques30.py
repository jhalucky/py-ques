def filter_strings(string):
    k = int(input("Enter the length of string: "))
    values = [i for i in string if len(i) >= k]
    return values


data = ["apple", "pie", "cherry", "banana", "kiwi", "pear"]
print(filter_strings(data))