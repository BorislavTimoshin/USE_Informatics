from re import findall

with open("24_3375.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:AA|CC)+", text)
    print(len(max(sequences, key=len)) // 2)


counter = 0
maxim = 0
for j in range(2):
    for i in range(j, len(text) - 1, 2):
        s = text[i] + text[i + 1]
        if s == "AA" or s == "CC":
            counter += 1
            maxim = max(maxim, counter)
        else:
            counter = 0
    counter = 0
print(maxim)
