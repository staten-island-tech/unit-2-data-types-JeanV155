# Step 1: Ask the user to input a sentence
sentence = input("Please enter a sentence: ")

# Step 2: Define a function to count words
def count_words(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Return the number of words
    return len(words)

# Step 3: Print the word count
word_count = count_words(sentence)
print(f"The number of words in your sentence is: {word_count}")