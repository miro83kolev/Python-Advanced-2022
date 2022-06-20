import re


def read_words():
    with open('./words.txt', 'r') as file:
        return file.read().split(' ')

def count_words_in_file(words):
    words_count = {
        word: 0 for word in words
    }

    with open('./input.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_count[word] += words_in_line.count(word.lower())

    return words_count

words_counts = count_words_in_file(read_words())
words_counts_sorted = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)

[print(f'{w} - {c}') for w, c in words_counts_sorted]
