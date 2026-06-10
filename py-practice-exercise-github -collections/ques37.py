# this one is also right!
# n = int(input("Enter starting countdown num: "))

# while n >= 0:
#     if n > 0:
#         print(n)

#     else:
#         print("Yeah! Let's fucking GO!")

#     n-=1


import time

count = int(input("Enter count: "))

while count > 0:
    print(count)
    time.sleep(1)
    count -= 1

print("Let's fucking GO!")