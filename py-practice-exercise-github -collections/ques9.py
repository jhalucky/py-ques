# string reversal
# str = "Python"

# print(str[::-1])

# count no of vowels in a sentence

vowels = 'aeiou'

str = "Priyanshi study hard and get a job and start feeding me"

counter = 0

for i in str.lower():
    if i in vowels:
        counter += 1 

print(counter)

