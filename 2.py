text = input('Введите текст: ')
text = text.lower()

words = list(text.split())

words_dict = {}

for word in words:
    words_dict[word] = words.count(word)

sorted_words = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)

print(sorted_words[:5])



