n = int(input("Enter the length of base and perpendicular: "))

for i in range(n,0,-1):
     if i == n or i == 1:
        print('* ' * i)
     else:
        print('* '  + '  '* (i-2) + '*')
                