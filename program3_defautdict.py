word_count = {}
for word in ["my","my","name","is","is","is","Hai"]:
    previous_count = word_count.get(word,0)
    word_count[word] = previous_count + 1
print(word_count)
