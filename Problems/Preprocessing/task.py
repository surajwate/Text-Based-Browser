sentence = input()

punctuation = [",", '.', '!', '?']

for symbol in punctuation:
    sentence = sentence.replace(symbol, '')

sentence = sentence.lower()
print(sentence)