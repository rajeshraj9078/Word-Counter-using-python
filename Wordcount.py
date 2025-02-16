def WordCounter(text:str) -> int:
    lines = text.split("\n")

    words = []
    for line in lines:
        print(line)
        for word in line.split(" "):
            words.append(word)
    return len(words)


lines = []
print("Enter your text: ")
while True:
    line = input()
    if not line:
        break
    lines.append(line)

words = WordCounter(str(lines))
print(f'Your text has {words} words.')