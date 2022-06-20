from string import punctuation
def count_symbols(line):
    punctuation_symbols = set(list(punctuation))
    letters_count = 0
    punctuation_count = 0
    for symbol in line:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuation_symbols:
            punctuation_count += 1
    return letters_count, punctuation_count

with open('text2.txt', 'r') as input_file, open('./output.txt', 'w') as output_file:
    for idx, line in enumerate(input_file):
        letters, punctuations = count_symbols(line)
        output_file.write(f'Line {idx + 1}: {line.strip()} ({letters})({punctuations})\n')