from random import shuffle

def sort_words(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parse the lines and sort the words
    words = []
    for line in lines:
        parts = line.strip().split(' - ')
        german_words = parts[0].split(', ')
        english_word = parts[1]
        base_word = german_words[0].split(' ')[1]
        words.append((base_word, german_words, english_word))
    # words.sort() # Sort alphabetically
    shuffle(words) # Sort randomly

    # Write the sorted words back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            line = ', '.join(word[1]) + ' - ' + word[2] + '\n'
            file.write(line)

# Use the function
sort_words('nouns.txt')
