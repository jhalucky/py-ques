# Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

# para = "Are you guys dumb or what? why did you park the bike there when you knew it is illegal to park there. I don't have single penny for this, and I want my bike now."
para = "apple banana apple cherry banana apple"

para2 = para.split()

dict = {}

for i in para2:
    # print(i, para2.count(i))
    if i in dict:
        dict[i] +=1

    else:
        dict[i] = 1

print(dict)


# 2nd method

# for i in para2:
#     dict[i] = para2.count(i)

# print(dict)