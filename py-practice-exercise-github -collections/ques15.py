email = input("Enter your email: ")

text = email.index("@")

username = email[0:text]

print(username)
print(text)