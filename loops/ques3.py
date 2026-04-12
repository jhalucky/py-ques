n = int(input("Enter the number: "))
table_of_n = 1

for i in range(1, 11):
    if i == 5:
        continue
    table_of_n = n * i
    print(n, "x", i, "=", table_of_n)