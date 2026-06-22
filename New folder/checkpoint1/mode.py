with open("sadow.slave.txt", "r") as file:

    text = file.read().lower()


text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

words = text.split()


word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
r.py