#довжина файлу у символах
with open("text.json", 'r') as file:
    text = file.read().strip().strip()
    len_chars = sum(len(word) for word in text)
    print(len_chars)