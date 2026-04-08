# Project 4 — Word Counter
# Author: your name here

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# TODO: total word count using len()
total_words = len(words)
# TODO: character count (no spaces)
# Hint: sentence.replace(" ", "") removes all spaces, then use len()
char_count = len (sentence.replace(" ", ""))
# TODO: word frequency dictionary
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
# TODO: print total words, total characters, then word frequency
print(f"\n--- Statistics ---")
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {char_count}")
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(f"'{word}': {count}")
