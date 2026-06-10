with open("py-practice-exercise-github -collections/sample.txt", "r") as file:
    content = file.read()
    print(content)

    text = content.split()
    words = []

    for i in text:
        words.append(i)
    
    print(f"The file conatins {len(words)} words")
    