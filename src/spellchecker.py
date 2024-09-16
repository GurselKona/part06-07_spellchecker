text = input("Write text:")
words = text.split()
with open("wordlist.txt") as f:
    dictionary = set(f.read().split())
checked = []
for word in words:
    if word.lower() not in dictionary:
        checked.append(f"*{word}*")
    else:
        checked.append(word)
print(" ".join(checked))