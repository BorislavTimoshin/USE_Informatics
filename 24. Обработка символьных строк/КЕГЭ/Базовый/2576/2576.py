from re import findall

with open("24_2576.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"[^.]+", text)
    print(len(max(sequences, key=len)))
