# Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result

text = input("Enter some text: ")

new_sentence = text.replace(" ","_")

print(new_sentence)