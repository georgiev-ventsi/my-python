# For a given sentence, return the average word length.

sentence1 = "Don't let another somber pariah consume your soul"
sentence2 = "Good things come to people who wait, but better things come to those who go out and get them."

def average_word_length(text):
    for n in "!?',;.\"":
        text = text.replace(n, '')
    words = text.split(' ')
    print(round(sum(len(word) for word in words)/len(words),2))

average_word_length(sentence1)
average_word_length(sentence2)