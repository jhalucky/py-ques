def count_vowels():
    s = input("Enter the word: ")
    vowels = "aeiouAEIOU"
    count = 0

    for i in s:
        if i in vowels:
            count += 1
    return count
    

print(count_vowels())