# Create a program that counts word occurrences in a string

def count_word_occurrences(text):
    words = text.lower().split()  
    word_count = {}

    for word in words:
        word = word.strip(".,!?")  
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


text = "Hello world! This is a test. Hello again, world."
word_counts = count_word_occurrences(text)

for word, count in word_counts.items():
    print(f"{word}: {count}")
