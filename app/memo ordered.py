import random

# For 'ß' press alt+0223
f = open("Wörter/L2 Wörter.txt", "r", -1, "utf-8")
words = []

for line in f:
    currentLine = line.split(" - ", 1)
    word_pair = [currentLine[0], [currentLine[1].strip(), 0]]
    words.append(word_pair)

f.close()

i = 0
while True:
    word_pair = words[i]
    RussianWord = word_pair[1][0]
    GermanWord = word_pair[0]

    print(RussianWord)
    userInput = input()

    if userInput == "exit":
        break
    elif userInput == GermanWord or userInput == "+":
        i += 1
    else:
        print("NB! -", GermanWord)
        word_pair[1][1] += 1
        if word_pair[1][1] == 3:
            i = 0
            print("\nOnce again from ground up 😉")
        input()
        print("\n" * 20)

    if i == len(words):
        break

print("\nWell done!🙂")
print("Practice makes perfect!")
print("Patience, persistence, concentration!\n")
