import random
# For 'ß' press alt+0223
f = open("Wörter/L8 Wörter.txt", "r", -1, "utf-8")
words = []
# basis = ["word", ["translation", 0]] ?
for line in f:
    currentLine = line.split(" - ", 1)
    # word_pair = basis ?
    word_pair = ["word", ["translation", 0]]
    word_pair[0] = currentLine[0]
    if "\n" in currentLine[1]:
        word_pair[1][0] = currentLine[1][:-1]
    else:
        word_pair[1][0] = currentLine[1]
    words.append(word_pair)
f.close()
direction = input("Show in German [G] or Russian [R]? ")
for word_pair in words:
    if direction == "G":
        word_pair[0], word_pair[1][0] = word_pair[1][0], word_pair[0]
    elif input() == "R":
        pass
# words = random.sample(words, 5)
while True:
    word_pair = random.choice(words)
    RussianWord = word_pair[1][0]
    GermanWord = word_pair[0]
    # score = word_pair[1][1]
    print(RussianWord)
    userInput = input()
    if userInput == "skip" or userInput == "+":
        del words[words.index(word_pair)]
        print("\n"*20)
    elif userInput == "exit":
        break
    elif userInput == GermanWord:
        word_pair[1][1] += 1
        print("\n"*20)
    else:
        print("NB! -", GermanWord)
        input()
        if word_pair[1][1] > -2:
            word_pair[1][1] -= 1
        print("\n"*20)
    if word_pair[1][1] == 1:
        del words[words.index(word_pair)]
    if len(words) == 0:
        break
print("\nWell done!🙂")
print("Practice makes perfect!")
print("Patience, persistence, concentration!\n")
